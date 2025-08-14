def create_cliente(conexao, dados):
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO Clientes (Nome_Cliente, Sobrenome_Cliente, RG, CPF, Telefone, Rua, Numero, Bairro, Cidade, Estado_UF)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', dados)
    conexao.commit()
    print("Cliente inserido com sucesso!")

def read_clientes(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)

def update_cliente(conexao, id_cliente, campo, novo_valor):
    cursor = conexao.cursor()
    sql = f"UPDATE Clientes SET {campo} = ? WHERE ID_Cliente = ?"
    cursor.execute(sql, (novo_valor, id_cliente))
    conexao.commit()
    print("Cliente atualizado com sucesso.")

def delete_cliente(conexao, id_cliente):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Clientes WHERE ID_Cliente = ?", (id_cliente,))
    conexao.commit()
    print("Cliente removido com sucesso.")

def buscar_cliente(conexao, termo):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE cpf = ? OR Nome_Cliente LIKE ?", (termo, f"%{termo}%"))
    resultados = cursor.fetchall()

    if resultados:
        for cliente in resultados:
            print(cliente)
    else:
        print("Nenhum cliente encontrado.")
