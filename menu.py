import sqlite3
from crud_clientes import create_cliente, read_clientes, update_cliente, delete_cliente

def menu():
    conexao = sqlite3.connect("database.db")
    
    while True:
        print("\n=== MENU CLIENTES ===")
        print("1. Inserir cliente")
        print("2. Ver todos os clientes")
        print("3. Atualizar cliente")
        print("4. Remover cliente")
        print("5. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            dados = []
            campos = ["Nome", "Sobrenome", "RG", "CPF", "Telefone", "Rua", "Número", "Bairro", "Cidade", "Estado"]
            for campo in campos:
                dados.append(input(f"{campo}: "))
            create_cliente(conexao, dados)

        elif opcao == "2":
            read_clientes(conexao)

        elif opcao == "3":
            id_cliente = input("ID do cliente a atualizar: ")
            campo = input("Campo que deseja atualizar (ex: Nome_Cliente): ")
            novo_valor = input("Novo valor: ")
            update_cliente(conexao, id_cliente, campo, novo_valor)

        elif opcao == "4":
            id_cliente = input("ID do cliente a remover: ")
            delete_cliente(conexao, id_cliente)

        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

    conexao.close()

menu()