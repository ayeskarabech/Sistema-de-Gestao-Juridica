# principal do Flask
# http://127.0.0.1:5000/ servidor web local

from flask import Flask, render_template # Flask → cria o app em si. É como ligar a “máquina” do servidor, e render_template → serve para renderizar (mostrar) arquivos HTML que estão na pasta templates/
from auth.routes import auth_bp # importa as rotas de autenticação do arquivo auth/routes.py

app = Flask(__name__) #cria o app Flask
app.secret_key = "segredo123"  # é uma chave usada pelo Flask para assinar e proteger os dados da session. se não tiver essa chave, qualquer pessoa poderia falsificar que está logado.
app.register_blueprint(auth_bp) # registra o blueprint de autenticação, que contém as rotas relacionadas ao login, logout, etc.

@app.route("/")  # Define a rota principal do site, que é o caminho / (raiz) 
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)  # Executa o servidor se rodar diretamente esse arquivo