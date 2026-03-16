# Arquitetura do Kleber AI

## Arquitetura Distribuída da Solução

O projeto utiliza uma **Arquitetura de Aplicações Distribuídas**, separando
a interface do usuário da lógica de negócio e das integrações externas.
Isso garante maior escalabilidade, independência entre camadas e
facilidade de manutenção.

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia | Função |
|--------|-----------|--------|
| Frontend | React + Vite | Interface web do assistente |
| Frontend | TypeScript | Tipagem estática e segurança |
| Frontend | Tailwind CSS | Estilização e design |
| Backend | Python + FastAPI | API, regras de negócio e orquestração |
| IA | Google Gemini API | Motor de linguagem natural |
| IA | Gemini CLI | Auxílio no desenvolvimento |
| Integração | Google Calendar API | Eventos e reuniões |
| Integração | Todoist API | Tarefas e to-do lists |
| Integração | Notion API | Notas e controle financeiro |
| Integração | Habitica API | Gamificação de hábitos |
| Infra | Docker | Containerização |
| Infra | GitHub Actions | CI/CD e automação de deploys |

---

## 📦 Estrutura de Camadas

### 🖥️ Frontend (React + Vite + TypeScript + Tailwind)
Responsável pela interface visual, exibindo:
- Chat com o assistente Kleber
- Timer Pomodoro integrado
- Widgets de produtividade (calendário, tarefas, notas)
- Dashboard de gamificação e hábitos

### ⚙️ Backend (Python + FastAPI)
Responsável por:
- Receber e processar requisições do frontend
- Orquestrar chamadas ao Gemini API
- Gerenciar todas as integrações externas
- Aplicar regras de negócio

### 🤖 Gemini API
Responsável por:
- Interpretar linguagem natural do usuário
- Decidir qual integração acionar
- Formatar respostas de forma humanizada e contextual

### 🔌 Integrações Externas

| Integração | API Gratuita | Função |
|-----------|-------------|--------|
| Google Calendar | ✅ Sim | Eventos e reuniões |
| Todoist | ✅ Sim (limitado) | Tarefas e listas |
| Notion | ✅ Sim | Notas e financeiro |
| Habitica | ✅ Sim | Gamificação |
| Pomodoro | ➖ N/A | Codado internamente |
| Dieta | ❌ Sem API | Controle manual |

---
