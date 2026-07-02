from menu import menu
from auth_control import PreviGestAuth

def rodar_sistema():
    auth = PreviGestAuth()
    
    while True:
        print("\n========================================")
        print("   PreviGest - Sistema de Gestão Nativo")
        print("========================================")
        print("1. Cadastrar Usuário (Novo Membro)")
        print("2. Fazer Login Híbrido")
        print("3. Sair")
        print("----------------------------------------")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            print("\n--- CADASTRO DE NOVO MEMBRO DA EQUIPE ---")
            nome = input("Nome Completo: ").strip()
            email = input("E-mail Corporativo: ").strip()
            handle = input("Handle do Usuário (ex: regina.adv): ").strip()
            senha = input("Digite a Senha: ").strip()
            
            print("\nSelecione o Cargo do Colaborador:")
            print("1. CEO")
            print("2. Administrador Principal")
            print("3. Advogado Associado")
            print("4. Estagiário")
            print("5. Contadora")
            print("6. Parceiro")
            
            cargo_opcao = input("Digite o número do cargo (1-6): ").strip()
            cargos_mapeados = {
                "1": "CEO",
                "2": "Administrador Principal",
                "3": "Advogado Associado",
                "4": "Estagiario",
                "5": "Contadora",
                "6": "Parceiro"
            }

            cargo = cargos_mapeados.get(cargo_opcao, "Advogado Associado")
            
            print(f"-> Cargo definido automaticamente como: {cargo}")
            
            # Executa o cadastro do usuário no supabase
            resultado = auth.cadastrar_usuario(nome, email, handle, senha, cargo, plano="Basico")
            
            if resultado["status"] == "sucesso":
                print(f"\n✅ {resultado['mensagem']}")
            else:
                print(f"\n❌ Erro: {resultado['mensagem']}")
                
        elif opcao == '2':
            print("\n--- LOGIN PREVIGEST ---")
            login_input = input("Digite seu E-mail ou @usuario: ").strip()
            senha_input = input("Digite sua Senha: ").strip()
            
            # Executa a busca na nuvem
            sucesso, mensagem, dados_usuario = auth.fazer_login(login_input, senha_input)
            
            if sucesso:
                print(f"\n🔓 {mensagem}")
                print(f"Plano Ativo: {dados_usuario['plano_saas'].upper()} | Cargo: {dados_usuario['cargo']}")
                
                # ENVIANDO OS DADOS DO BANCO PARA O MENU NATIVO
                menu(dados_usuario) 
            else:
                print(f"\n🔒 Falha no Login: {mensagem}")
                
        elif opcao == '3':
            print("\nEncerrando o PreviGest... Até logo!")
            break
        else:
            print("\n⚠️ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    rodar_sistema()