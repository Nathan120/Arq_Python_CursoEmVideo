def leiaint(string):
    while True:
        num = input(f'{string}: ')
        if num.isnumeric() == True:
            break
        else:
            print('\033[;31m Erro! Digite um número inteiro \033[m')
    return num


n = leiaint('Digite um número')
print(f'Você acabou de digitar no numero {n}')