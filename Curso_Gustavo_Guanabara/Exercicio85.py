total = list()
for i in range(1,8):
    total.append(int(input(f'Digite o {i}º valor : ')))
total.sort()
for p in total:
    if p%2 == 0:
        print(f'Par {p}')
    else:
        print(f'Impar {p}')