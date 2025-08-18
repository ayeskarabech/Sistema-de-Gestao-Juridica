import sqlite3 # database connection

def conectar(): # Conectar ao banco de dados
    conexao = sqlite3.connect("database.db")
    conexao.row_factory = sqlite3.Row  # Isso permite acessar colunas pelo nome, como um dicionário. o row_factory deixa o retorno mais fácil de ler como dicionários(user["usuario"] em vez de índice)
    return conexao

def criar_tabela(): # Criar tabela no banco de dados
    conexao = conectar()
    cursor = conexao.cursor()

    # Tabela com dados dos clientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clientes(
        ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT, 
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

    # Tabela de usuários para login
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        usuario TEXT PRIMARY KEY,
        senha_hash BLOB NOT NULL,  -- é BLOB porque o bcrypt gera bytes, não string.
        tipo_acesso TEXT NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criar_tabela()
    print("Banco e tabela criados com sucesso.")