'''from time import sleep
for i in range(10, -1,-1):
    print(i)
    sleep(1)
print('BOMW')
sleep(0.5)
print('CABUM')'''
s = 0
c = 0
for i in range(3,500,3):
    if i%2 == 1:
        s += i
        c += 1
print('A soma entre os {} numeros multiplos de 3 é igual a {}'.format(c,s))