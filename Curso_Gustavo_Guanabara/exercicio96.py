def area(a, b):
    s = a * b
    print(f'A área de um terreno {a}x{b} é de = {s} m²')


# Progama principal
print('-' * 30)
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(comp, larg)
