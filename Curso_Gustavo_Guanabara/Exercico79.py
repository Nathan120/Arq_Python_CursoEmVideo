ista = list()
cont = 0
while True:
    num = int(input('Digite um número: '))
    if num not in ista:
        ista.append(num)
    else:
        print('!O número já está na lista!')
    op = input('Deseja adicionar outro numero?[S/N]: ')
    if op in 'Nn':
        break
ista.sort()
print(f'Os numeros cadastardos são {ista} ')
