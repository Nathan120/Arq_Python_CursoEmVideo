def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} no campeonato')


jogador = input('Nome do jogador: ')
ng = input('Número de gols marcados: ')
print(ficha(jogador, ng))
