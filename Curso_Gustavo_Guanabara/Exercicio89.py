lista = list()
ficha = list()
print('-'*20)
print('   Escola Dueto')
print('-'*20)
while True:
    lista.append(str(input('Digite seu 1ª nome = ')))
    lista.append(float(input('Digite a 1ª nota: ')))
    lista.append(float(input('Digite a 2ª nota: ')))
    media = (lista[1] + lista[2])/ 2
    lista.append(media)
    ficha.append(lista[:])
    lista.clear()
    op = str(input('Deseja cadastra outro aluno?[S/N]: '))
    if op in 'Nn':
        break
print('-='*15)
for n in range(0,len(ficha)):
    if n == 0:
        print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
    print(f'{n:<4}{ficha[n][0].capitalize():<10}{ficha[n][3]:>8.2f}')
while True:
    opc = int(input('Deseja ver a nota de qual aluno?[999 para sair]: '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    print(f'As notas de  {ficha[opc][0].capitalize()} foram: {ficha[opc][1:3]}')
