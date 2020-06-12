def notas(*num, sit=False):
    """
    -> Função usada para receber várias notas é retorna alguns paremetros como:
    0. Total
    1. Maior nota
    2. Menor nota
    3. Media da turma
    4. E a situação [opcional]
    :param num: Notas
    :param sit: [opcional]
    :return: dicionario com os paremetros(meiorNota, menorNota, media, situação[opcional])
    """
    dados = dict()
    dados['Total'] = len(num)
    soma = tot = 0
    for c in num:
        if tot == 0:
            dados['maior'] = c
            dados['menor'] = c
        else:
            if dados['maior'] < c:
                dados['maior'] = c
            if dados['menor'] > c:
                dados['menor'] = c
        tot += 1
        soma += c
    dados['média'] = soma / tot
    if sit == True:
        if dados['média'] < 6:
            dados['situação'] = 'RUIM!'
        elif dados['média'] >= 7:
            dados['situação'] = 'BOA'
        else:
            dados['situação'] = 'RAZOAVEL'
    return dados


resp = notas(5.5, 8, 5, 6.5, sit= True)
print(resp)
help(notas)