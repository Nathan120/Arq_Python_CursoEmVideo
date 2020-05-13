while True:
    print('-----\033[4;33;40mConversor\033[m-------\n')
    num = int(input('Digite um número = '))
    ecolha = int(input('''Escolha na tabela a conversão desejada
            [1] Binário
            [2] Octal
            [3] Hexadecimal
            = '''))
    if ecolha==1:
        print('O número em binario {}'.format(bin(num)[2:]))
    elif ecolha==2:
        print('O número em octal {}'.format(oct(num)[2:]))
    elif ecolha==3:
        print('O número em hexadecimal  {}'.format(hex(num)[2:]))
    else:
        print('Você não escolheu uma opção valida!!')
    rep = input('Deseja cont ? [s/n]= ')
    if rep =='n':
        break