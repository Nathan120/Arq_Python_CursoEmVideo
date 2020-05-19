import random
nome = str('Mega sena')
lista = list()
print('-='*15)
print(f'         \033[7;34m{nome}\033[m')
print('-='*15)
njogos = int(input('Deseja gerar quantos jogos?: '))
for i in range(0,njogos):
    for j in range(0,7):
        lista.append(random.randint(1,60))
    print(f'{i+1}ª JOGO: {lista}')
    lista.clear()