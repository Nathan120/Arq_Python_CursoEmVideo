import random
maior = menor = 0
tabela = (random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9))
for i in range(0,5):
    num = tabela[i]
    if i == 0:
        print('Os numeros sorteados foram:',end= ' ')
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    print(num, end= ' ')
print('\n')
print(f'O maior número sorteado foi {maior}')
print(f'O menor número sorteado foi {menor}')