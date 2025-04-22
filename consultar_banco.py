from models import db, Projeto

# Verificar se há registros na tabela
print(Projeto.query.all())

# Exibir os títulos dos projetos
for projeto in Projeto.query.all():
    print(projeto.titulo, projeto.descricao)
