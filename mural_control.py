from database import conectar_supabase

class PreviGestMural:
    def __init__(self):
        self.supabase = conectar_supabase()

    def postar_recado(self, autor_id, mensagem, area="Geral", is_fixado=False):
        """ Publica um novo aviso no mural do escritório """
        if not self.supabase:
            return {"status": "erro", "mensagem": "Sem conexão com o banco."}

        payload = {
            "autor_id": autor_id,
            "mensagem": mensagem,
            "area": area,
            "is_fixado": is_fixado
        }

        try:
            self.supabase.table("mural_recados").insert(payload).execute()
            return {"status": "sucesso", "mensagem": f"Recado publicado na área [{area}]!"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro ao publicar no mural: {e}"}

    def listar_mural_por_area(self, area_filtro=None):
        """ 
        Lista os recados trazendo o nome do autor. 
        Se passar uma área (ex: 'Financeiro'), filtra apenas os recados dela.
        """
        if not self.supabase:
            return []

        try:
            # Puxa o nome do usuário que postou o recado
            consulta = self.supabase.table("mural_recados").select("id, mensagem, area, is_fixado, created_at, usuarios(nome_completo, usuario_handle)")
            
            # Ordena primeiro pelos fixados e depois pelos mais recentes
            consulta = consulta.order("is_fixado", desc=True).order("created_at", desc=True)

            if area_filtro and area_filtro != "Geral":
                consulta = consulta.eq("area", area_filtro)

            resposta = consulta.execute()
            return resposta.data
        except Exception as e:
            print(f"Erro ao ler mural: {e}")
            return []

    def responder_recado(self, recado_pai_id, autor_id, resposta_texto):
        """ Cria um comentário/resposta em uma thread de recado existente """
        if not self.supabase:
            return {"status": "erro", "mensagem": "Sem conexão com o banco."}

        payload = {
            "recado_pai_id": recado_pai_id,
            "autor_id": autor_id,
            "resposta": r_texto
        }

        try:
            self.supabase.table("mural_respostas").insert(payload).execute()
            return {"status": "sucesso", "mensagem": "Resposta enviada para a thread!"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro ao responder: {e}"}