from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Definição da tabela "projetos"
class Projeto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    imagem = db.Column(db.String(200), nullable=True)  # Caminho da imagem (opcional)

    def __repr__(self):
        return f'<Projeto {self.titulo}>'
