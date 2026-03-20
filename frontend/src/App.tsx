import { useState } from 'react'

const CLIENT_ID = import.meta.env.VITE_GOOGLE_CLIENT_ID
const SCOPE = 'https://www.googleapis.com/auth/drive.readonly'

export default function App() {
  const [status, setStatus] = useState('')
  const [result, setResult] = useState('')

  function openDrivePicker() {
    const tokenClient = (window as any).google.accounts.oauth2.initTokenClient({
      client_id: CLIENT_ID,
      scope: SCOPE,
      callback: (tokenResponse: any) => {
        const gapi = (window as any).gapi
        gapi.load('picker', () => {
          const google = (window as any).google
          const picker = new google.picker.PickerBuilder()
            .addView(google.picker.ViewId.DOCS)
            .setOAuthToken(tokenResponse.access_token)
            .setCallback((data: any) => {
              if (data.action === 'picked') {
                const file = data.docs[0]
                handleFile(file.id, file.name, tokenResponse.access_token)
              }
            })
            .build()
          picker.setVisible(true)
        })
      },
    })
    tokenClient.requestAccessToken()
  }

  async function handleFile(fileId: string, fileName: string, token: string) {
    setStatus(`Baixando "${fileName}"...`)
    setResult('')

    const res = await fetch(`https://www.googleapis.com/drive/v3/files/${fileId}?alt=media`, {
      headers: { Authorization: `Bearer ${token}` },
    })
    const blob = await res.blob()

    const formData = new FormData()
    formData.append('file', blob, fileName)

    setStatus('Transcrevendo...')
    const transcribeRes = await fetch('http://localhost:8000/transcribe', {
      method: 'POST',
      body: formData,
    })
    const { transcription, txt_path } = await transcribeRes.json()

    setStatus('')
    setResult(`Transcrição concluída!\n\nArquivo salvo em:\n${txt_path}\n\n---\n\n${transcription}`)
  }

  return (
    <div style={{ maxWidth: 800, margin: '40px auto', padding: '0 20px', fontFamily: 'sans-serif' }}>
      <h1>Kleber AI — Análise de Reuniões</h1>

      <button onClick={openDrivePicker} style={{ padding: '10px 20px', fontSize: 16, cursor: 'pointer' }}>
        Selecionar arquivo do Google Drive
      </button>

      {status && <p style={{ marginTop: 20, color: '#555' }}>{status}</p>}

      {result && (
        <pre style={{ marginTop: 20, whiteSpace: 'pre-wrap', background: '#f5f5f5', padding: 20, borderRadius: 8 }}>
          {result}
        </pre>
      )}
    </div>
  )
}
