# Sistema de Gestão Jurídica
 Projeto pessoal fullstack, criado com o objetivo de aprender na prática os fundamentos de um sistema real e gerar impacto direto para uso jurídico. Construído em Python, Flask e SQLite.

Desenvolvido por Ayeska Rabech – Estudante de Sistemas de Informação na UFRPE (Universidade Federal Rural de Pernambuco), com apoio de orientação técnica baseada em metodologias ágeis e práticas de desenvolvimento profissional.

Objetivos:

- Estudar e aplicar conhecimentos reais de backend com Python e Flask;
- Desenvolver um projeto completo: backend, frontend, banco de dados, análises e deploy;
- Criar um case sólido para meu portfólio visando vagas de estágio e desenvolvimento futuro.
- Este projeto que será meu espaço de crescimento técnico, prático e pessoal, onde posso testar, errar, aprender e evoluir de verdade.

Tecnologias Utilizadas:

- **Backend**: Python, Flask, SQLite3, Pandas, Matplotlib, datetime, smtplib/yagmail  
- **Frontend**: HTML, CSS, Jinja2, JavaScript (básico), Bootstrap (opcional)  
- **APIs (futuro)**: Twilio API (WhatsApp), Google Calendar API  
- **Banco de dados na nuvem (futuro)**: Supabase (PostgreSQL)  
- **Deploy**: Render, Railway, Vercel  
- **Outros**: Git, GitHub, Notion, Scrum adaptado

Funcionalidades:

- Cadastro de clientes (nome, CPF, tipo de benefício etc.)
- Listagem de clientes com visual web
- Login com senha criptografada (`hashlib`)
- Busca por CPF ou nome
- Agenda de movimentações por cliente
- Análise de dados com Pandas (aniversariantes, pré-aposentadoria, ...)
- Gráficos com Matplotlib (tipo de benefício, idade,...)
- Dashboard analítico
- Exportação para Excel (.xlsx ou .csv)
- Notificações por e-mail e WhatsApp
- Sistema de permissões por tipo de usuário
- Integração com Google Calendar
- Deploy completo com banco em nuvem (Supabase)

Etapas do Desenvolvimento:

O projeto foi dividido em **fases**, organizadas no estilo ágil (Scrum + Sprints), com entregas semanais e retrospectivas.

Você pode acompanhar todas as fases no [Notion do Projeto](https://www.notion.so/PreviGest-SISTEMA-DE-GEST-O-PREVIDENCI-RIA-23b562eeda348006814fd3b475b96e09) ou na [timeline de commits](#).

Como Executar Localmente:

```bash
# 1. Clone o repositório
git clone https://github.com/ayeskarabech/Sistema-de-Gestao-Juridica.git
cd previgest

# 2. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Rode o sistema
python app.py