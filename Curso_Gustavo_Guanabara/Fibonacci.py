q = int(input('Quantos números deseja saber de FIb = '))
n = p = 1
n2 = 0
c = 0
while c < q:
    print(p, end='... ')
    p = n + n2
    n2 = n
    n = p
    c += 1