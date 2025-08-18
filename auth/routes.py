# guarda as rotas /login, /logout, /register
# Blueprint cria mini “apps” separados para as rotas, ele não muda como o Flask funciona, só deixa mais limpo e organizado.
# autenticação no navegador (login/logout) é feita com sessões (session)

from flask import Blueprint, render_template, flash, request, redirect, url_for, session
''' Explicação rápida:
- Blueprint → é como um “mapa” que organiza as rotas do Flask, tipo uma pasta que guarda tudo sobre autenticação.
- render_template → serve para renderizar (mostrar) arquivos HTML que estão na pasta templates/
- request → pega as informações que vêm do navegador → ex: o que o usuário digitou no formulário.
- redirect → manda o usuário pra outra rota, tipo “depois do login, vá para /home”.
- url_for → gera o caminho de uma rota pelo nome da função, em vez de escrever a URL direto (boas práticas).
- session → uma “mochila invisível” que o servidor dá pro usuário e guarda informações enquanto ele está navegando (ex: se ele está logado ou não). '''
import sqlite3, bcrypt
from database import conectar

auth_bp = Blueprint("auth", __name__, template_folder="../templates/auth") # define o Blueprint para as rotas de autenticação. Traduzindo: “Oi Flask, cria pra mim um pacote de rotas chamado auth, que tem seus templates guardados em /templates/auth/.”

@auth_bp.route("/login", methods=["GET", "POST"]) # Define a rota /register para cadastro de usuários
def login():
    if request.method == "POST":
        usuario = request.form["usuario"] # pega o valor digitado no campo <input name="usuario"> do register.html
        senha = request.form["senha"]

        # buscar usuario no banco de dados e usar a função conectar() do database.py para evitar repetição de código:
        conexao = conectar()
        cursor = conexao.cursor()
        user = cursor.execute(
            "SELECT usuario, senha_hash, tipo_acesso FROM usuarios WHERE usuario = ?",
            (usuario,)).fetchone() # fetchone é útil quando você espera que a consulta retorne apenas uma linha ou quando você quer processar os resultados um de cada vez.
        conexao.close()

        if user and bcrypt.checkpw(senha.encode("utf-8"), user["senha_hash"]): # verifica se o usuário existe, se o SELECT retornou algo e se a senha bate
            session["usuario"] = user["usuario"] #guarda o nome de usuário na session (espécie de "mochila" que acompanha o usuário logado).
            session["tipo_acesso"] = user["tipo_acesso"]
            return redirect(url_for("index"))

        flash("Usuário ou senha inválidos")
        return redirect(url_for("auth.login"))

    return render_template("auth/login.html")

# rota de logout
@auth_bp.route("/logout")
def logout():
    session.pop("usuario", None)
    session.pop("tipo_acesso", None)  # remove também o tipo de acesso
    return redirect(url_for("auth.login"))
    
# rota de cadastro
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        tipo_acesso = request.form["tipo_acesso"]

        senha_hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())

        conexao = conectar()
        cursor = conexao.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuarios (usuario, senha_hash, tipo_acesso) VALUES (?, ?, ?)",
                (usuario, senha_hash, tipo_acesso))
            conexao.commit()
        except sqlite3.IntegrityError: # IntegrityError é um erro do SQLite que acontece quando você tenta inserir um valor que já existe (ex: usuário duplicado)
            flash("Usuário já existe!")
            return redirect(url_for("auth.register"))
        finally:
            conexao.close()
        flash("Usuário cadastrado com sucesso!")
        
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")