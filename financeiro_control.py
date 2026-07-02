from database import conectar_supabase

class PreviGestFinanceiro:
    def __init__(self):
        self.supabase = conectar_supabase()

    def registrar_lancamento(self, tipo, recebedor_pagador, categoria, data_vencimento, valor, status="Pendente", usuario_id=None):
        """ Registra uma entrada (ex: honorários) ou saída (ex: despesa) no banco """
        if not self.supabase:
            return {"status": "erro", "mensagem": "Sem conexão com o banco."}

        payload = {
            "tipo": tipo,
            "recebido_pago_para": recebedor_pagador,
            "categoria": categoria,
            "data_vencimento": data_vencimento,
            "valor": float(valor),
            "status_pagamento": status,
            "criado_por": usuario_id
        }

        try:
            self.supabase.table("financeiro_lancamentos").insert(payload).execute()
            return {"status": "sucesso", "mensagem": f"{tipo} de R$ {valor:.2f} registrada com sucesso!"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro ao salvar lançamento financeiro: {e}"}

    def obter_fluxo_caixa(self):
        """ Puxa todos os lançamentos para calcular o total de entradas, saídas e o saldo """
        if not self.supabase:
            return {"entradas": 0, "saidas": 0, "saldo": 0, "dados": []}

        try:
            resposta = self.supabase.table("financeiro_lancamentos").select("*").execute()
            dados = resposta.data

            entradas = sum(float(item['valor']) for item in dados if item['tipo'] == 'Entrada' and item['status_pagamento'] == 'Efetuado')
            saidas = sum(float(item['valor']) for item in dados if item['tipo'] == 'Saida' and item['status_pagamento'] == 'Efetuado')
            
            return {
                "entradas": entradas,
                "saidas": saidas,
                "saldo": entradas - saidas,
                "dados": dados
            }
        except Exception as e:
            print(f"Erro ao calcular fluxo de caixa: {e}")
            return {"entradas": 0, "saidas": 0, "saldo": 0, "dados": []}