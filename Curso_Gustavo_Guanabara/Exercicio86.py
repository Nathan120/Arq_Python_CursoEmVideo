matriz = [[0,0,0],[0,0,0],[0,0,0]]
somat = soma3 = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]= int(input(f'\033[7mDigite um valor para [{l},{c}]:\033[m '))
        somat += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]

for l in range(0,3):
    for c in range(0,3):
        print(f'\033[7;32m{matriz[l][c]:2}\033[m', end=' ')
        if l == 1:
            if maior < matriz[1][c]:
                maior = matriz[1][c]
    print()
print(f'A soma total dos números digitados é {somat}')
print(f'A soma dod valores da 3ª coluna {soma3}')
print(f'O maior valor da 2ª linha {maior}')