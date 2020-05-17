lista = list()
impar = []
par = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    op = input('Deseja adicionar outro numero?[S/N]: ')
    if op in 'Nn':
        break
for i in range(0,len(lista)):
    if lista[i]%2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
print(f'A lista completa {lista}')
print(f'Os números pares inseridos são {par}')
print(f'Os números impares inseridos são {impar}')