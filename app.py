# principal do Flask

from flask import Flask, render_template # Flask → cria o app em si. É como ligar a “máquina” do servidor, e render_template → serve para renderizar (mostrar) arquivos HTML que estão na pasta templates/
from auth.routes import auth_bp # importa as rotas de autenticação do arquivo auth/routes.py
from clientes.routes_clientes import clientes_bp # importa as rotas de clientes do arquivo clientes/routes.clientes.py

app = Flask(__name__) #cria o app Flask
app.secret_key = "segredo123"  # é uma chave usada pelo Flask para assinar e proteger os dados da session. se não tiver essa chave, qualquer pessoa poderia falsificar que está logado.
app.register_blueprint(auth_bp) # registra o blueprint de autenticação, que contém as rotas relacionadas ao login, logout, etc.
app.register_blueprint(clientes_bp) # registra o blueprint de clientes, que contém as rotas relacionadas aos clientes.

@app.route("/")  # Define a rota principal do site, que é o caminho / (raiz) 
def index():
    return render_template("index.html") # render_template() é usada no Flask para renderizar arquivos de template HTML, ela combina o conteúdo do arquivo de template com dados fornecidos pelo código Python, gerando o código HTML final que será enviado ao navegador do usuário. 
if __name__ == "__main__":
    app.run(debug=True)  # Executa o servidor se rodar diretamente esse arquivo