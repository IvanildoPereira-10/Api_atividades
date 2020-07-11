from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Pereira', idade=39)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Ivanildo').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Pereira').first()
    pessoa.nome = 'Alves'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Alves').first()
    pessoa.delete()

if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
