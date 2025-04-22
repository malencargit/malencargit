from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do Banco de Dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de Projeto
class Projeto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)

# Criar tabelas no banco de dados
with app.app_context():
    db.create_all()

# Página inicial
@app.route("/")
def home():
    return render_template("index.html")

# Página de projetos
@app.route("/projetos")
def lista_projetos():
    projetos = Projeto.query.all()
    return render_template("projetos.html", projetos=projetos)

# Rota para executar um projeto (simulação)
@app.route("/executar/<int:projeto_id>", methods=["POST"])
def executar_projeto(projeto_id):
    projeto = Projeto.query.get_or_404(projeto_id)
    
    # Aqui você pode colocar a lógica de execução do projeto
    print(f"Executando projeto: {projeto.titulo}")

    return redirect(url_for('lista_projetos'))  # Redireciona de volta à lista de projetos

if __name__ == "__main__":
    app.run(debug=True)
