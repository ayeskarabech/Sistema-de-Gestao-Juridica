# o terminal nao é o foco, e o auth daqui nao esta conectado com o auth do flask/routes.
'''
from menu import menu
from auth import cadastrar_usuarios, fazer_login
from database import criar_tabela

criar_tabela()  # Cria o banco de dados e as tabelas necessárias

if __name__ == "__main__":
    while True:
        print("Bem-vindo ao sistema de gestão jurídica!")
        print("1. Cadastrar usuário")
        print("2. Fazer login")
        print("3. Sair")   
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            u = input("Digite o nome de usuário: ")
            s = input("Digite a senha: ")
            tipo_acesso = input("Digite o tipo de acesso (admin/usuario): ")
            cadastrar_usuarios(u, s, tipo_acesso)
        elif opcao == '2':
            u = input("Digite o nome de usuário: ")
            s = input("Digite a senha: ")
            sucesso, tipo_acesso = fazer_login(u, s)
            if sucesso:
                print(f"Bem-vindo, {u}! Tipo de acesso: {tipo_acesso}")
                menu()  # Só chama o menu após login bem-sucedido
            else:
                print("Falha no login.")
        elif opcao == '3':
            print("Saindo do sistema. Até logo!")
            break