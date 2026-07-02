# PreviGest - Sistema de Gestão Jurídica 

💡 **A Origem do Projeto: Do Problema Real à Solução Técnica**
A ideação do **PreviGest** nasceu no coração de um escritório de advocacia previdenciária real. Ele foi provocado pela insatisfação e exaustão da minha irmão que é advogada previdenciarista, diante do cenário atual de softwares jurídicos: a necessidade de pagar por múltiplas assinaturas de sistemas fragmentados para gerenciar um único fluxo de trabalho. Era um sistema para clientes, outro para cálculos, outro para mural de tarefas... 

Além do custo inflacionado, a grande frustração era a falta de inteligência analítica: os sistemas de mercado guardavam os dados, mas poucos entregavam insights limpos, claros e dicas concisas que auxiliassem de verdade na tomada de decisões estratégicas baseadas na própria base de dados do escritório.

O intuito do PreviGest, **por enquanto**, é unificar esse ecossistema, integrar ferramentas essenciais e alavancar a gestão e a produtividade do escritório dela em uma única plataforma inteligente.

---

Então, **PreviGest** é um ecossistema de software que o projeto nasceu como uma aplicação fullstack inicial e evoluiu para uma solução de arquitetura moderna, combinando persistência em nuvem, controle rígido de acessos (SaaS) e um assistente inteligente de IA focado na produtividade jurídica.

Desenvolvido por **Ayeska Silva** – Estudante de Sistemas de Informação na UFRPE.

---

### Histórico de Evolução e Versões

Abaixo está mapeada a trajetória de engenharia do sistema, documentando o amadurecimento das escolhas arquiteturais da aplicação:

| Versão | Descrição | Stack Utilizada | Paradigma / Infraestrutura | Status |
| :---: | :--- | :--- | :--- | :---: |
| **1.0** | **Monolito Web Inicial:** Protótipo estruturado para aprendizado de rotas, autenticação básica e persistência relacional local. | Python, Flask, SQLite3, HTML5, CSS3, Jinja2, Bootstrap, bcrypt | Aplicação Web Local | Concluído ✅ |
| **2.0** | **Prototipagem de Interface:** Design do ecossistema visual e mapeamento de componentes focados na experiência do usuário (UX/UI). | Stitch, Google AI Studio | Prototipagem & Prompt Engineering | Concluído ✅ |
| **2.1** | **Migração de Dados (Escalabilidade):** Substituição do armazenamento local por um banco relacional gerenciado e escalável. | PostgreSQL, Supabase | Cloud Database Architecture | Concluído ✅ |
| **2.2** | **Refatoração do Backend & Segurança:** Reestruturação completa do core em Python para suporte a Desktop, blindagem de credenciais por variáveis de ambiente e regras SaaS. | Python 3, `google-generativeai`, Supabase Client | Desktop Backend Engine | Concluído ✅ |
| **2.3** | **Integração Visual (Próxima Fase):** Acoplamento do motor lógico do backend com a interface gráfica final. | CustomTkinter, Antigravity | Desktop GUI Integration | **Próximo Passo** |

---

### Funcionalidades Atuais (Módulos Operacionais)

* **Autenticação & SaaS:** Sistema de login criptografado integrado ao Supabase, decodificando metadados de permissão baseados em Cargos (*Estagiário*, *Advogado*) e Planos (*Básico*, *Pro*, *Premium*).
* **Gerenciamento de Clientes:** CRUD completo conectado ao PostgreSQL em nuvem para cadastro, listagem e auditoria de processos jurídicos.
* **Mural de Recados Pro:** Central interna para comunicação síncrona de avisos e fixação de tarefas importantes para a equipe.
* **Central Financeira:** Monitoramento ativo do fluxo de caixa corporativo (entradas/saídas) com cálculo automatizado de saldo consolidado.
* **Calculadora Previdenciária:** Simulador técnico de regras comuns de transição por Tempo de Contribuição e pontuações pós-reforma.
* **Hub Inteligente IA PreviMind:** Motor cognitivo conectado à API do Gemini para varredura avançada de jurisprudência (teses e precedentes) e geração parametrizada de minutas processuais.

---

### Boas Práticas e Segurança Aplicadas

* **Variáveis de Ambiente:** Nenhuma credencial do Supabase ou chave do Gemini é exposta no código. O sistema isola os segredos em um arquivo local protegido.
* **Versionamento Limpo:** O histórico do repositório é auditado para garantir a conformidade com as diretrizes de segurança da informação (SecOps).

