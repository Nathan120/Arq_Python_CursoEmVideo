import random
from time import sleep
itens = ('Pedra','Papel','Tesoura')
pc = random.randint(0,2)
print('-=-=-=-=-=-=-=-=-=-=-=-=-')
print('     JOGO DA VELHA       ')
print('-=-=-=-=-=-=-=-=-=-=-=-=-\n')
print("""Escolha sua jogada
        [0] \033[7mPedra\033[m
        [1] \033[7mPapel\033[m
        [2] \033[7mTesoura\033[m""")
op = int(input(': '))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO')

print('-=-=-=-=-=-=-=-=-=-=-')
print('Pc = {}'.format(itens[pc]))
print('Jogador = {}'.format(itens[op]))
print('-=-=-=-=-=-=-=-=-=-=-')

if pc == 0:
    if op == 0:
        print('\033[7mEMPATE\033[m')
    elif op == 1:
        print('Jogador GANHOU')
    elif op == 2:
        print('Pc GANHOU')
    else:
        print('\033[4;33;41mOpção inválida!\033[m')
elif pc == 1:
    if op == 0:
        print('PC GANHOU')
    elif op == 1:
        print('\033[7mEMPATE\033[m')
    elif op == 2:
        print('JOGADOR GANHOU')
    else:
        print('\033[4;33;41mOpção inválida!\033[m')
else:
    if op == 0:
        print('JOGADOR GANHOU')
    elif op == 1:
        print('PC GANHOU')
    elif op == 2:
        print('\033[7mEMPATE\033[m')
    else:
        print('\033[4;33;41mOpção inválida!\033[m')