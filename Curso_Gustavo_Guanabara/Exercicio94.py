pessoa = dict()
total = list()
totp = tidade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite seu nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Sua idade: '))
    total.append(pessoa.copy())
    totp += 1
    tidade += pessoa['idade']
    while True:
        op = input('Desseja continuar [S/N]?: ').upper()[0]
        if op in 'SN':
            break
        print('ERRO!, Digite apenas S ou N.')
    if op == 'N':
        break
media = tidade/totp
print('-=' * 30)
print(f'Temos {totp} pessoas cadastradas')
print(f'A média de idades da pessoas cadastradas foi de {media:5.2f}')
print('As mulheres cadastradas foram: ', end='')
for p in total:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=',')
print()

print('A lista das pessoas acima da média: ', end='')
for p in total:
    if total['idade'] > media:
        print('   ')
        for k,v in p.items():
            print(f'{k} = {v}')
        print()
print('<<ENCERRADO>>')