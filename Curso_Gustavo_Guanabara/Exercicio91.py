from time import sleep
import random
from operator import itemgetter
dados = dict()
ranking = dict()
maior = 0
for j in range(1,5):
    num = random.randint(1,6)
    dados[f'Jogador{j}'] = num
    print(f'Jogador Nº{j} tirou {num}')
    #sleep(2)
print('-'*15)
print('Ranking dos jogadores:')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for f,v in enumerate(ranking):
    print(f'{f+1}º lugar =  {v[0]} tirou {v[1]}')