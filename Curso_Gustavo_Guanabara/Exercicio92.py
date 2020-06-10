from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - ano
dados['ctps'] = int(input('Carteira de Trabalho(0 não tem): '))
if dados['ctps'] != 0:
    dados['contrat'] = int(input('Digite o seu ano de contratação: '))
    dados['salario'] = float(input('Digite seu salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrat'] + 35) - datetime.now().year)
print('-='*30)

for k,v in dados.items():
    print(f'{k} tem o valor {v}')