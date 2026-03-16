# Fluxo do Kleber AI

## Visão Geral

O Kleber recebe comandos via duas interfaces:
- Interface Web → Chat direto na aplicação
- Bot Telegram → Mensagens de texto e áudio

---

## Canais de Entrada

| Canal | Tipo de Input | Processamento |
|-------|--------------|---------------|
| Interface Web | Texto | Direto ao Backend |
| Bot Telegram | Texto | Direto ao Backend |
| Bot Telegram | Áudio | Transcrição → Backend |

---

## Fluxo Principal

Usuário → Interface Web ou Bot Telegram
Bot Telegram com áudio → Transcrição → Backend
Bot Telegram com texto → Backend
Interface Web com texto → Backend
Backend → Gemini API → Interpreta intenção
Gemini → Entendeu tudo → Executa ação e confirma
Gemini → Entendeu parcial → Avisa o que faltou e sugere
Gemini → Não entendeu → Avisa e sugere como reformular

---

## Intenções e Integrações

| Exemplo de Comando | Intenção | Integração |
|-------------------|----------|-----------|
| "Kleber, gastei 100 reais na padaria" | Registrar gasto | Notion (Financeiro) |
| "Kleber, marcar reunião com Izabela dia X hora Y" | Criar evento | Google Calendar |
| "Kleber, combinei de sair com Stela dia X hora Y" | Criar evento pessoal | Google Calendar |
| "Kleber, me lembrar de fazer lista de compras" | Criar lembrete | Todoist |
| "Kleber, iniciar pomodoro" | Timer foco | Pomodoro Interno |
| "Kleber, completei minha meta de hoje" | Registrar hábito | Habitica |

---

## Fluxos Detalhados

### Fluxo Feliz (Entendeu tudo)

Usuário fala: "Kleber, gastei 100 reais na padaria agora"
Gemini identifica a intenção como registrar gasto, valor R$100,00, local padaria e data hoje
Backend chama Notion API e registra o gasto
Kleber responde: "Anotado! R$ 100,00 na padaria registrado no seu financeiro."

---

### Fluxo Parcial (Entendeu parcialmente)

Usuário fala: "Kleber, marcar reunião com Izabela"
Gemini identifica intenção criar evento e pessoa Izabela, mas não encontra data e hora
Kleber responde: "Entendi que você quer marcar uma reunião com a Izabela!
Só faltou a data e a hora.
Tente assim: Kleber, reunião com Izabela dia 20/07 às 14h"

---

### Fluxo de Erro (Não entendeu)

Usuário fala: "Kleber, aquela coisa lá"
Gemini não identifica nenhuma intenção clara
Kleber responde: "Hmm, não consegui entender o que você precisa!
Posso te ajudar com:
- Registrar gastos → gastei X reais em Y
- Criar eventos → marcar reunião com X dia Y hora Z
- Criar tarefas → me lembrar de X
- Pomodoro → iniciar pomodoro
Tente novamente!"

---

## Fluxo Telegram com Áudio

Usuário envia áudio no Telegram
Bot Telegram recebe o áudio
Áudio passa pela transcrição via Whisper ou Gemini
Kleber confirma: "Entendi: gastei 100 reais na padaria. Processando..."
Segue o fluxo normal de intenção

---

## Lembretes e Notificações

| Tipo | Canal | Exemplo |
|------|-------|---------|
| Lembrete de tarefa | Telegram + Web | "Lembrete: fazer lista de compras!" |
| Evento próximo | Telegram + Web | "Em 30min: reunião com Izabela" |
| Meta do dia | Telegram | "Você ainda não registrou seus hábitos hoje!" |
| Resumo diário | Telegram | "Resumo do dia: X tarefas, R$Y gastos" |

---

## Contexto de Conversa

O Kleber mantém memória da sessão atual, entendendo referências
como "ela", "isso" e "aquele evento".

Exemplo:
Usuário: "Kleber, marcar reunião com Izabela dia 20 às 14h"
Kleber: "Reunião marcada!"
Usuário: "Muda pra 15h"
Kleber: "Reunião com Izabela atualizada para 15h!"