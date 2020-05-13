maior = menor = pme = pma = 0
valores = list()
for c in range(0,5):
    valores.append(int(input('Digite um número = ')))

for c, v in enumerate(valores):
    if c == 0:
        maior = v
        menor = v
    else:
        if v > maior:
            maior = v
            pma = c
        if v < menor:
            menor = v
            pme = c
print(valores)
print(f'O maior valor é {maior} que está na posição {pma}')
print(f'O menor valor é {menor} que está na posição {pme}')
print('\033[7m fim \033[m')