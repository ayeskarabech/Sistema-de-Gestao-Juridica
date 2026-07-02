from clientes import PreviGestClientes
from mural_control import PreviGestMural
from financeiro_control import PreviGestFinanceiro
from calculadora_control import PreviGestCalculadora
from previmind_control import PreviMindEngine

def menu(dados_usuario_logado=None):
    gerenciador_clientes = PreviGestClientes()
    mural = PreviGestMural()
    financeiro = PreviGestFinanceiro()
    calculadora = PreviGestCalculadora()
    ai_engine = PreviMindEngine()
    
    user_id = dados_usuario_logado.get("id") if dados_usuario_logado else "00000000-0000-0000-0000-000000000000"
    user_tier = dados_usuario_logado.get("plano_saas") if dados_usuario_logado else "Basico"
    user_role = dados_usuario_logado.get("cargo") if dados_usuario_logado else "Estagiario"

    while True:
        print("\n========================================")
        print("   PREVIGEST - PAINEL OPERACIONAL")
        print("========================================")
        print("1. Cadastrar Novo Cliente")
        print("2. Listar Clientes e Casos")
        print("3. Abrir Mural de Recados Pro")
        print("4. Central Financeira (Fluxo de Caixa)")
        print("5. Calculadora Previdenciária (Técnica)")
        print("6. Hub Inteligente IA PreviMind")
        print("7. Voltar para o Menu Inicial")
        print("----------------------------------------")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            nome = input("Nome do Cliente: ").strip()
            cpf_cnpj = input("CPF/CNPJ: ").strip()
            telefone = input("WhatsApp: ").strip()
            res = gerenciador_clientes.cadastrar_novo_cliente(nome, cpf_cnpj, telefone)
            print(f"\n{res['mensagem']}")
            
        elif opcao == '2':
            print("\n--- LISTA DE CLIENTES ---")
            lista = gerenciador_clientes.listar_clientes_cadastrados()
            for idx, cli in enumerate(lista, 1):
                print(f"{idx}. {cli['nome_completo']} | Reg: {cli.get('oab', 'N/A')}")
                
        elif opcao == '3':
            print("\n--- MURAL DE RECADOS PRO ---")
            print("1. Visualizar Quadro de Avisos")
            print("2. Fixar Novo Recado na Equipe")
            mural_op = input("Escolha uma opção do Mural: ").strip()
            
            if mural_op == '1':
                print("\n[Mural] Buscando avisos ativos na nuvem...")
                avisos = mural.listar_avisos_mural()
                if not avisos:
                    print("Nenhum aviso fixado no momento.")
                for idx, aviso in enumerate(avisos, 1):
                    print(f"{idx}. [{aviso['data_postagem']}] {aviso['autor']}: {aviso['conteudo']}")
            
            elif mural_op == '2':
                conteudo = input("Digite o texto do recado: ").strip()
                # Passa o cargo/nome do usuário logado como autor do aviso
                res_mural = mural.fixar_novo_aviso(autor=user_role, texto=conteudo)
                print(f"\n{res_mural['mensagem']}")

        elif opcao == '4':
            print("\n--- CENTRAL FINANCEIRA ---")
            print("1. Ver Fluxo de Caixa (Saldo & Lançamentos)")
            print("2. Registrar Nova Entrada/Saída")
            fin_op = input("Escolha uma opção financeira: ").strip()
            
            if fin_op == '1':
                print("\n[Financeiro] Puxando extrato consolidade do Supabase...")
                fluxo = financeiro.obter_fluxo_caixa()
                print(f"========================================")
                print(f" SALDO ATUAL DO ESCRITÓRIO: R$ {fluxo['saldo_total']:.2f}")
                print(f"========================================")
                for lanc in fluxo['historico']:
                    tipo_sinal = "[+]" if lanc['tipo'] == 'entrada' else "[-]"
                    print(f"{tipo_sinal} R$ {lanc['valor']:.2f} | {lanc['descricao']} ({lanc['data']})")
            
            elif fin_op == '2':
                descricao = input("Descrição do lançamento: ").strip()
                valor = float(input("Valor (R$): ").replace(',', '.'))
                tipo = input("Tipo (entrada/saida): ").strip().lower()
                
                res_fin = financeiro.registrar_transacao(descricao, valor, tipo, user_id)
                print(f"\n{res_fin['mensagem']}")

        elif opcao == '5':
            print("\n--- CALCULADORA PREVIDENCIÁRIA ---")
            print("1. Simular Aposentadoria por Tempo de Contribuição")
            print("2. Simular Transição por Pontos")
            calc_op = input("Escolha o tipo de cálculo: ").strip()
            
            idade = int(input("Idade atual do cliente: "))
            tempo_contrib = int(input("Tempo de contribuição (em anos): "))
            sexo = input("Sexo (M/F): ").strip().upper()
            
            if calc_op == '1':
                res_calc = calculadora.calcular_tempo_comum(idade, tempo_contrib, sexo)
                print(f"\n[Resultado da Simulação]:")
                print(f" Faltam {res_calc['anos_restantes']} anos para atingir a regra comum.")
                print(f" Estimativa de Concessão: {res_calc['ano_estimado']}")
                
            elif calc_op == '2':
                res_pontos = calculadora.calcular_regra_pontos(idade, tempo_contrib, sexo)
                print(f"\n[Resultado da Regra por Pontos]:")
                print(f" Pontuação Atual: {res_pontos['pontos_atuais']} pontos.")
                print(f" Status: {res_pontos['status_direito']}")
                    
        elif opcao == '6':
            while True:
                print("\n--- CENTRAL HUB IA PREVIMIND ---")
                print("1. Pesquisa Avançada de Jurisprudência (Plano Pro)")
                print("2. Gerador Inteligente de Petições por Pastas (Plano Premium)")
                print("3. Voltar ao Painel")
                
                ai_op = input("Escolha um módulo do PreviMind: ").strip()
                
                if ai_op == '1':
                    print("\n--- VARREDURA JURÍDICA INTELIGENTE ---")
                    termo = input("Digite a tese ou termo jurídico (Ex: Aposentadoria Especial Metalúrgico): ").strip()
                    res_ai = ai_engine.search_jurisprudence_ai(termo, user_tier)
                    
                    if res_ai["status"] == "success":
                        print("\n[Resultado Encontrado]:")
                        print(f" Tese:      {res_ai['extracted_thesis']}")
                        print(f" Precedente:{res_ai['applicable_precedent']}")
                        print(f" Sumário IA:{res_ai['ai_summary']}")
                    else:
                        print(f"\nAcesso Negado: {res_ai['message']}")
                        
                elif ai_op == '2':
                    print("\n--- ROBÔ GERADOR DE DOCUMENTOS ---")
                    print("Selecione a pasta de destino:")
                    print("1. Documentos Iniciais (Procuração/Contrato)")
                    print("2. Petições Iniciais de Concessão")
                    pastas = {"1": "Documentos Iniciais", "2": "Peticoes Iniciais de Concessao"}
                    p_escolha = input("Opção da pasta: ").strip()
                    pasta_nome = pastas.get(p_escolha, "Geral")
                    
                    doc_nome = input("Nome/Espécie do benefício (Ex: BPC LOAS, Salario Maternidade): ").strip()
                    cli_vinc = input("Nome do Cliente para vincular: ").strip()
                    
                    context = {"client_name": cli_vinc}
                    res_doc = ai_engine.generate_document_by_folder(pasta_nome, doc_nome, context, user_tier)
                    
                    if res_doc["status"] == "success":
                        print(f"\nDocumento [{res_doc['document_title']}] gerado na pasta [{res_doc['folder_destination']}]!")
                        print("------------------------------------------------")
                        print(res_doc["preview_content"])
                        print("------------------------------------------------")
                    else:
                        print(f"\nAcesso Negado: {res_doc['message']}")
                        
                elif ai_op == '3':
                    break
                    
        elif opcao == '7':
            break