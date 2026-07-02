from database import conectar_supabase
import bcrypt

class PreviGestAuth:
    def __init__(self):
        self.supabase = conectar_supabase()

    def formatar_handle(self, usuario_input):
        usuario_input = usuario_input.strip().lower()
        if "@" in usuario_input and "." in usuario_input:
            return usuario_input  # Permanece e-mail
        if not usuario_input.startswith("@"):
            return f"@{usuario_input}"
        return usuario_input

    def cadastrar_usuario(self, nome, email, handle, senha, cargo, plano="Basico"):
        if not self.supabase:
            return {"status": "erro", "mensagem": "Sem conexão com o banco."}

        # 1. Validação de Limite de Usuários do Plano SaaS
        # Contamos quantos usuários já existem cadastrados no banco
        resposta_contagem = self.supabase.table("usuarios").select("id", count="exact").execute()
        total_existente = resposta_contagem.count if resposta_contagem.count is not None else 0

        limites = {"Basico": 5, "Pro": 15, "Premium": 25}
        if total_existente >= limites.get(plano, 5):
            return {
                "status": "erro", 
                "mensagem": f"Limite atingido! O plano {plano} permite no máximo {limites[plano]} usuários."
            }

        # 2. Criptografia de senha com bcrypt
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        handle_formatado = self.formatar_handle(handle)

        # 3. Inserção na tabela do Supabase
        dados_usuario = {
            "nome_completo": nome,
            "email": email,
            "usuario_handle": handle_formatado,
            "cargo": cargo,
            "plano_saas": plano
        }
        
        try:
            # Aqui fazemos a inserção na nuvem
            self.supabase.table("usuarios").insert(dados_usuario).execute()
            return {"status": "sucesso", "mensagem": f"Usuário {handle_formatado} criado!"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro ao cadastrar: {e}"}

    def fazer_login(self, login_input, senha_input):
        if not self.supabase:
            return False, "Sem conexão com o banco.", None

        identificador = self.formatar_handle(login_input)
        
        # Determina se a busca será por e-mail ou por @handle
        coluna = "email" if ("@" in identificador and "." in identificador) else "usuario_handle"

        try:
            # Busca o usuário correspondente na tabela
            resposta = self.supabase.table("usuarios").select("*").eq(coluna, identificador).execute()
            
            if not resposta.data:
                return False, "Usuário ou e-mail não encontrado.", None
                
            usuario = resposta.data[0]
            
            # TODO: Em produção, faremos a checagem do hash da senha armazenado em uma tabela de credenciais separada.
            # Por enquanto, retornamos os dados de perfil e nível do plano
            return True, f"Bem-vindo, {usuario['nome_completo']}!", usuario
            
        except Exception as e:
            return False, f"Erro na autenticação: {e}", None