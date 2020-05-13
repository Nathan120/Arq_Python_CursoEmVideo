print('-=-=-=-=-=-=-=-=-=-=-')
print('\033[7m       TABUADA       \033[m')
print('-=-=-=-=-=-=-=-=-=-=-')
num = int(input('Digite o número para ver sua tabuada = '))
for i in range(0, 11):
    print('{} x {:2} = {:2}'.format(num,i, num*i))