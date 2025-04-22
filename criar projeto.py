from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, Projeto

app = Flask(__name__)

# Configuração do Banco de Dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados
db.init_app(app)

# Criar o banco de dados e tabelas (rodar uma vez)
with app.app_context():
    db.create_all()

# Página inicial
@app.route("/")
def home():
    projetos = Projeto.query.all()  # Busca todos os projetos no banco
    return render_template("index.html", projetos=projetos)

# Página de projetos
@app.route("/projetos")
def lista_projetos():
    projetos = Projeto.query.all()
    return render_template("projetos.html", projetos=projetos)

if __name__ == "__main__":
    app.run(debug=True)
