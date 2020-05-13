from time import sleep
n1 = int(input('Digite um número = '))
n2 = int(input('Digite outro número = '))
op = ''
while op != '5':
    print(' Numeros {} e {} '.format(n1,n2))
    op = input("""\033[4;33;41m------Menu-------\033[m
    [1] Soma
    [2] Multiplicar
    [3] Maior valor
    [4] Novos números
    [5] Sair 
    = """)
    if op == '1':
        print('{} + {} = {}'.format(n1,n2,n1 + n2))
        sleep(3)
    elif op == '2':
        print('{} * {} = {}'.format(n1,n2,n1*n2))
        sleep(3)
    elif op == '3':
        if n1 > n2:
            print('{} é maior que {}'.format(n1,n2))
            sleep(3)
        else:
            print('{} é maior que {}'.format(n2, n1))
            sleep(3)
    elif op == '4':
        n1 = int(input('Digite um número = '))
        n2 = int(input('Digite outro número = '))
    elif op == '5':
        print('')
    else:
        print('Opção inválida')
print('Fim do progama')
sleep(1)
print('\033[4;32;44mTCHAU\033[m')