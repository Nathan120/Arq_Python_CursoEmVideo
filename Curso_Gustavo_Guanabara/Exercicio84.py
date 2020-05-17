final = list()
dados = list()
total = maior = menor = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Peso: ')))
    final.append(dados[:])
    if total == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if maior < dados[1]:
            maior = dados[1]
        if menor > dados[1]:
            menor = dados[1]
    total += 1
    dados.clear()
    op = str(input('Deseja adicionar mais dados? [S/N]: '))
    if op in 'Nn':
        break
print(f'Ao todo foram cadastrados {total} pessoas')
for i in final:
    if i[1] == maior:
        print(f'O maior pesso foi {maior:.2f}Kg. Peso de {i[0]}')
    if i[1] == menor:
        print(f'O menor peso foi {menor:.2f}kg. Peso de {i[0]}')