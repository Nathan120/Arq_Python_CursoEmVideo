num = int(input('Digite um número = '))
c = 0
for i in range(1,num + 1):
    if num%i == 0:
        print('\033[;33m{}\033[m'.format(i), end=' ')
        c += 1;
    else:
        print('\033[;31m{}\033[m'.format(i), end=' ')
print('\nO numero {} foi divisivel {} vezes'.format(num,c))
if c == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é PRIMO')
