from database import conectar_supabase

class PreviGestClientes:
    def __init__(self):
        self.supabase = conectar_supabase()

    def cadastrar_novo_cliente(self, nome, cpf_cnpj, telefone, etiquetas=None):
        """
        Cadastra um cliente no banco de dados. 
        Note que usamos os campos mapeados na tabela 'usuarios' ou uma futura tabela de contatos.
        """
        if not self.supabase:
            return {"status": "erro", "mensagem": "Sem conexão com o banco."}

        dados_cliente = {
            "nome_completo": nome,
            "telefone": telefone,
            "oab": cpf_cnpj,
            "cargo": "Parceiro",
            "usuario_handle": f"@{nome.lower().replace(' ', '')}"
        }

        try:
            self.supabase.table("usuarios").insert(dados_cliente).execute()
            return {"status": "sucesso", "mensagem": f"Cliente {nome} cadastrado com sucesso na nuvem!"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro ao salvar cliente: {e}"}

    def listar_clientes_cadastrados(self):
        """ Recupera a lista de contatos do escritório do Supabase """
        if not self.supabase:
            return []

        try:
            resposta = self.supabase.table("usuarios").select("nome_completo", "telefone", "oab").execute()
            return resposta.data
        except Exception as e:
            print(f"Erro ao listar clientes: {e}")
            return []