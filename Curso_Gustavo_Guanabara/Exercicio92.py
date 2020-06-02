from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - ano
dados['ctps'] = int(input('Carteira de Trabalho(0 não tem): '))

print(dados)