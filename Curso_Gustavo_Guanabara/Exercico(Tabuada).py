print('----------TABUADA------')
while True:
    escolha = int(input('Ecolha o número para mostra na Tabela(0-9) = '))
    if escolha == 0:
        for i in range(11):
            print('{} x {} = {}'.format(escolha, i, escolha*i))
    if escolha == 1:
        for i in range(11):
            print('{} x {} = {}'.format(escolha, i, escolha*i))
    if escolha == 2:
        for i in range(11):
            print('{} x {} = {}'.format(escolha, i, escolha*i))
    if escolha == 3:
        for i in range(11):
            print('{} x {} = {}'.format(escolha, i, escolha*i))
    if escolha == 4:
        for i in range(11):
            print('{} x {} = {}'.format(escolha, i, escolha*i))
    if escolha == 5:
        for i in range(11):
            print('{} x {} = {}'.format(escolha, i, escolha*i))
    if escolha == 6:
        for i in range(11):
            print('{} x {} = {}'.format(escolha, i, escolha*i))
    if escolha == 7:
        for i in range(11):
            print('{} x {} = {}'.format(escolha, i, escolha*i))
    if escolha == 8:
        for i in range(11):
            print('{} x {} = {}'.format(escolha, i, escolha*i))
    if escolha == 9:
        for i in range(11):
            print('{} x {} = {}'.format(escolha, i, escolha*i))
    if escolha == 10:
        for i in range(11):
            print('{} x {} = {}'.format(escolha, i, escolha*i))
    saida = input('Deseja Fazer mais uma operação?[s/n]')
    if saida == 'n':
        break
