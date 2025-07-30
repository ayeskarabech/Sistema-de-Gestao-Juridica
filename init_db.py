import sqlite3

# Conecta/cria banco
conexao = sqlite3.connect("database.db")  # cria um banco de dados
cursor = conexao.cursor()

# Criação da tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes(
    Nome_Cliente TEXT NOT NULL,
    Sobrenome_Cliente TEXT NOT NULL,
    RG TEXT NOT NULL,
    CPF TEXT NOT NULL,
    Telefone TEXT,
    Rua TEXT,
    Numero TEXT,
    Bairro TEXT,
    Cidade TEXT,
    Estado_UF TEXT
    )
''')

conexao.commit()
conexao.close()

print("Banco e tabela criados com sucesso.")