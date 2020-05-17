lista = list()
cont = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont += 1
    op = input('Deseja adicionar outro numero?[S/N]: ')
    if op in 'Nn':
        break
lista.sort(reverse=True)
print(f'foram adicionados {cont} números na lista')
print(f'A lista em ordem decrescente {lista}')
if 5 in lista:
    print('O Numero 5 está na lista')
else:
    print('O número 5 não está ma lista')