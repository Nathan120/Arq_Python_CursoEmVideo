try:
    a = int(input('Numero:'))
    b = int(input('Denominador:'))
    r = a/b
except Exception as erro:
    print('Infelixxmente tivemos um problema :(')
    print(f' O problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('tchau')
