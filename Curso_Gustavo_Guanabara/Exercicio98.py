def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= (-1)
    if inicio < fim:
        for p in range(inicio, fim+1, passo):
            print(p, end='...')
        print()
    elif inicio > fim:
        for p in range(inicio, fim-1, -passo):
            print(p, end='...', flush= True)
        print()


# Progama principal
contador(1, 10, 1)
contador(10, 0, 2)

print('-' * 30)
print('Agora é sua vez !')
inicio = int(input('Inicio = '))
fim = int(input('Fim = '))
passo = int(input('Passo = '))
contador(inicio, fim, passo)
