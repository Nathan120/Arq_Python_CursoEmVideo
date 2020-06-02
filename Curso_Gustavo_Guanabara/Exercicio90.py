ficha = dict()
ficha['Nome'] = str(input('NOME: '))
ficha['Média']= float(input(f'Qual a média de {ficha["Nome"].capitalize()}: '))
if ficha['Média'] >= 7:
    ficha['Situaçao'] = 'Aprovado'
else:
    ficha['Situação'] = 'Reprovado'
for f,v in ficha.items():
    print(f'{f} {v}')
