from time import sleep


def pyhelp(func):

    escreva(f"Acessando o manual do camando '{func}' ", 0, 30, 44)
    sleep(2)
    print(f'\033[7;30m', end='')
    help(func)
    print('\033[m', end='')


def escreva(txt, S=0, T=0, B=0):
    quant = len(txt) + 4
    print(f'\033[{S};{T};{B}m', end='')
    print('~'*quant)
    print(f'  {txt}')
    print('~' * quant)
    print('\033[m', end='')


# Progama principal
while True:
    escreva('Sistema de Ajuda PyHelp ', 0, 30, 42)
    escolha = input('Digite uma Função ou Biblioteca: ')
    if escolha == 'fim' or escolha == 'Fim':
        escreva('Até logo', 0, 30, 41)
        sleep(2)
        break
    pyhelp(escolha)
