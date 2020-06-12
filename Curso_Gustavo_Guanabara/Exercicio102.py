def fatorial(num= 1, show = False):
    if show == False:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f
    else:
        f = 1
        for c in range(num, 0, -1):
            f *= c
            print(f' {c}', end=' ')
            if c != 1:
                print('x', end='')
        print(' =', end=' ')
        return f


print(fatorial(5, True))