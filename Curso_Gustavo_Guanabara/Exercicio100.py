import random


def sorteio(val):
    """
    -> Sortei 5 números para uma lista
    :param val: Lista que vai receber os números
    :return: Sem retorno
    """
    print('Sorteando 5 valores para a lista: ', end='')
    for i in range(0,5):
        sort = random.randint(0, 5)
        print(sort, end=' ')
        val.append(sort)
    print('PRONTO!')


def somap(val):
    soma = 0
    for num in val:
        if num%2 == 0:
            soma += num
    print(f'Somando os valores pares de {val}, temos {soma}')


# Progama principal
valores = list()
sorteio(valores)
somap(valores)
help(sorteio)