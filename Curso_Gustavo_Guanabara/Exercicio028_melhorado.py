import random

n = random.randrange(0,5)
n2 = int(input('Digite um número = '))
c = 1
if n2 == n:
    print('Você acertou o número que o pc escolheu ')
    print('Seu numero foi {} o que do pc {} '.format(n2, n))
    print('Foi necessario apenas {} tentativa para acertar'.format(c))
while n != n2:
    print('Você errou o número que o pc escolheu ')
    print('Seu numero foi {} o que do pc {} '.format(n2, n))
    n = random.randrange(0, 5)
    n2 = int(input('Digite um número = '))

    c += 1
    if n == n2:
        print('Você acertou o número que o pc escolheu ')
        print('Seu numero foi {} o que do pc {} '.format(n2, n))
        print('Foi necessario {} tentativas para acertar'.format(c))