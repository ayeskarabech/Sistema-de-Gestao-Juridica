<h2>Sistema de Gestão Jurídica (PreviGest)</h2>

Projeto pessoal fullstack criado com o objetivo de aprender na prática os fundamentos de um sistema real. Desenvolvido em Python, Flask e SQLite, este sistema será expandido gradualmente com backend, frontend, análises e deploy. Desenvolvido por Ayeska Rabech – Estudante de Sistemas de Informação (UFRPE).

**Objetivos**

- Estudar e aplicar conhecimentos reais de backend com Python e Flask;
- Desenvolver um projeto completo: backend, frontend, banco de dados, análises e deploy;
- Criar um case sólido para portfólio visando desenvolvimento futuro;
- Ser um espaço de crescimento técnico e prático, onde posso testar, errar, aprender e evoluir.

**Tecnologias Utilizadas**

- Backend: Python, Flask, SQLite3, bcrypt
- Frontend: HTML, CSS, Jinja2, JavaScript (básico), Bootstrap
- *planos futuros*: 
- APIs: Twilio API (WhatsApp), Google Calendar API
- Banco de dados em nuvem: Supabase (PostgreSQL)
- Deploy: Render, Railway, Vercel
- Outros: Git, GitHub, Notion, Scrum adaptado

**Funcionalidades (em desenvolvimento)**

- Cadastro e listagem de clientes
- Login com senha criptografada (bcrypt)
- Busca por CPF ou nome
- Sistema de permissões por tipo de usuário (admin, advogado, estagiário etc.)
- Dashboard analítico (futuro)
- Exportação para Excel/CSV (futuro)
- Notificações por e-mail/WhatsApp (futuro)
- Integração com Google Calendar (futuro)

**Como Executar Localmente**
```
# 1. Clone o repositório
git clone https://github.com/ayeskarabech/Sistema-de-Gestao-Juridica.git
cd Sistema-de-Gestao-Juridica

# 2. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
.\venv\Scripts\activate    # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o servidor Flask
python app.py

# 5. Acesse no navegador
http://127.0.0.1:5000/
```


**Etapas do Desenvolvimento**

O projeto está sendo desenvolvido em fases semanais no estilo ágil (Scrum + Sprints):
- Autenticação de usuários (login, registro, logout)✅
- Estrutura inicial de clientes (listagem e cadastro parcial)✅
- Próximos passos: CRUD completo de clientes e conexão ao banco
- Futuro: dashboards, análises, notificações e deploy

**Aplicação Real**

Este sistema será testado e utilizado em um escritório de advocacia previdenciária real, ajudando na:
- Organização completa de atendimentos e cadastro de clientes;
- Agilidade no envio de atualizações via WhatsApp/e-mail;
- Análise de métricas da empresa (clientes ativos, tipos de processos, aniversariantes, taxa de sucesso etc.).

**Prints e Demonstrações**

Sessão em construção! Em breve com imagens de telas, formulários e gráficos.


> Nota pessoal: Desenvolver algo do zero exige paciência, pesquisa e constância.
> Mesmo um sistema simples pode gerar impacto quando nasce de uma necessidade real.
