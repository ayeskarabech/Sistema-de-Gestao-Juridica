# autenticação no terminal
# usando apenas a autenticação no navegador, de /auth/routes.py
'''
import sqlite3
import bcrypt
from database import conectar

def cadastrar_usuarios(usuario, senha, tipo_acesso):
    conexao = conectar()
    cursor = conexao.cursor()

    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()) # gerando salt + senha hash. encode converte de string para bytes, e gensalt gera um salt aleatório.
    
    try: 
        cursor.execute('''
            INSERT INTO usuarios (usuario, senha_hash, tipo_acesso)
            VALUES (?, ?, ?)
        ''', (usuario, senha_hash, tipo_acesso))
        conexao.commit()
        print(f"Usuário '{usuario}' cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print(f"Erro: O usuário '{usuario}' já existe.")
    finally:
        conexao.close()

def fazer_login(usuario, senha):
    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()  

    cursor.execute('''
        SELECT senha_hash, tipo_acesso FROM usuarios WHERE usuario = ?
    ''', (usuario,))
    resultado = cursor.fetchone() # .fetchone() busca a senha do usuário, pega apenas a primeira linha que bate com a consulta. Se não encontrar nada, retorna None
    conexao.close()

    if resultado:
        senha_hash_cadastrada, tipo_acesso = resultado
        if bcrypt.checkpw(senha.encode(), senha_hash_cadastrada):  # checkpw verifica se a senha informada bate com o hash armazenado
            print(f"Login bem-sucedido! Tipo de acesso: '{tipo_acesso}'!")
            return True, tipo_acesso
        else:
            print("Senha incorreta.")
            return False, None
    else:
        print("Usuário não encontrado.")
        return False, None
'''