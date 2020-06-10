dados = dict()
gol = list()
todos = list()
tot = cod = 0
while True:
    dados.clear()
    dados['cod'] = cod
    dados['nome'] = str(input('Nome do Jogador = '))
    part = int(input('Quantas partidas {} jogou: '.format(dados['nome'])))
    for c in range(0,part):
        gol.append(int(input(f'Quatos gols na partida {c+1} ?: ')))
        tot += gol[c]
    dados['gols'] = gol[:]
    dados['total'] = tot
    todos.append(dados.copy())
    cod += 1
    tot = 0
    gol.clear()
    op = str(input('Deseja continuar? [S/N] = '))
    if op in 'Nn':
        break
print('-=' * 30)
print('cod  nome        gols        total')
for p in todos:
    for v in p.values():
        print(f'{v}', end=' ')
    print()


'''print('-=' * 30)
for k,v in dados.items():
    print(f' {k} tem o valor {v}')

print('-=' * 30)

print(f'O jogador {dados["nome"]} jogou {part} partidas')
i = 0
for i,v in enumerate(dados['gols']):
    print(f'  => na partida {i}, fez {v} gols')
    i += 1
print(f'Foi um total de {dados["total"]} gols')'''