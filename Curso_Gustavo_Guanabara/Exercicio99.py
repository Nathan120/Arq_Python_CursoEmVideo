def maior(*num):
    tot = len(num)
    m = cont = 0
    #m = num[0] aqui não funcioa quando não tem paramentros
    print('-=' * 30)
    print('Analisando os valores passados...')
    for p in num:
        print(p, end=' ')
        if m == cont:
            m = p
        if m < p:
            m = p
    print(f' Foram informados {tot} valores ao todo.')
    print(f'O maior valor informado foi {m}.')
    print('-=' * 30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(2, 1)
maior(6)
maior()








