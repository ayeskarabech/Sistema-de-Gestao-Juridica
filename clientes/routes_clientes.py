from flask import Blueprint, render_template, request, redirect, url_for, flash

clientes_bp = Blueprint("clientes", __name__, template_folder="../templates/clientes") # define o Blueprint para as rotas de clientes.

clientes = []  # Lista para armazenar os clientes enqt nao conecta ao banco de dados

@clientes_bp.route("/clientes")
def listar_clientes():
    return render_template("clientes/listar_clientes.html", clientes=clientes)

@clientes_bp.route("/clientes/novo", methods=["GET", "POST"])
def novo_cliente():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        clientes.append({"nome": nome, "email": email, "telefone": telefone})
        flash("Cliente adicionado com sucesso!")
        return redirect(url_for("clientes.listar_clientes"))
    return render_template("clientes/novo_cliente.html")