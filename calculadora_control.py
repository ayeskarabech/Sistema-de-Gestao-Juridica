from database import conectar_supabase

class PreviGestCalculadora:
    def __init__(self):
        self.supabase = conectar_supabase()

    def salvar_historico_calculo(self, cliente_nome, tipo_calculo, usuario_id):
        """ 
        Salva o registro de um planejamento previdenciário gerado no escritório.
        Ex de tipos: 'Concessao RGPS', 'Revisao da Vida Toda', 'Analise BPC/LOAS'.
        """
        if not self.supabase:
            return {"status": "erro", "mensagem": "Sem conexão com o banco de dados."}

        payload = {
            "cliente_nome": cliente_nome,
            "tipo_calculo": tipo_calculo,
            "criado_por": usuario_id
        }

        try:
            self.supabase.table("calculos_recentes").insert(payload).execute()
            return {"status": "sucesso", "mensagem": f"Cálculo de {tipo_calculo} para {cliente_nome} salvo no histórico!"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro ao salvar histórico de cálculo: {e}"}

    def listar_historico_recente(self, usuario_id=None):
        """ 
        Recupera os últimos cálculos realizados para exibir no painel da calculadora.
        """
        if not self.supabase:
            return []

        try:
            consulta = self.supabase.table("calculos_recentes").select("id, cliente_nome, tipo_calculo, updated_at")
            
            # Ordena pelos cálculos mais recentes modificados
            consulta = consulta.order("updated_at", desc=True)
            
            resposta = consulta.execute()
            return resposta.data
        except Exception as e:
            print(f"Erro ao buscar histórico de cálculos: {e}")
            return []

    def gerar_dados_relatorio_timbrado(self, calculo_id):
        """
        Simula a exportação estruturada dos dados para alimentar o gerador de relatórios 
        com o timbre do escritório.
        """
        if not self.supabase:
            return None

        try:
            resposta = self.supabase.table("calculos_recentes").select("*").eq("id", calculo_id).execute()
            if resposta.data:
                dados = resposta.data[0]
                # Estrutura os dados formais para o documento
                return {
                    "cabecalho": "PREVIGEST - ADVOCACIA PREVIDENCIÁRIA",
                    "documento_tipo": f"RELATÓRIO TÉCNICO DE PLANEJAMENTO: {dados['tipo_calculo'].upper()}",
                    "cliente": dados['cliente_nome'],
                    "data_emissao": dados['updated_at'][:10],
                    "status_validacao": "Assinado Digitalmente pelo Agente IA PreviMind"
                }
            return None
        except Exception as e:
            print(f"Erro ao gerar dados do relatório: {e}")
            return None