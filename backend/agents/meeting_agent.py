import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """Você é um assistente especializado em análise de reuniões corporativas.

Preciso que você:

1. TRANSCREVA o áudio desta reunião de forma clara e organizada,
identificando os participantes quando possível (Ex: "Pessoa 1:",
"Pessoa 2:" ou pelo nome, se identificável).

2. Após a transcrição, apresente um RESUMO EXECUTIVO contendo:

✅ PONTOS PRINCIPAIS DISCUTIDOS
- Liste os temas centrais abordados

🎯 DECISÕES TOMADAS
- O que foi definido ou aprovado durante a reunião

📌 AÇÕES E RESPONSÁVEIS (Action Items)
- Tarefa | Responsável | Prazo (se mencionado)

⚠️ PONTOS DE ATENÇÃO
- Problemas, riscos ou pendências levantados

📅 PRÓXIMOS PASSOS
- O que foi combinado para os próximos encontros

Organize tudo de forma clara, objetiva e fácil de compartilhar com a equipe."""


def analyze_meeting(transcription: str) -> str:
    """Recebe a transcricao e retorna o resumo estruturado da reuniao."""
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": f"Aqui está a transcrição da reunião:\n\n{transcription}"}
        ]
    )
    return message.content[0].text
