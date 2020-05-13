num = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','trese','quatorze','quinze','deseseis','desesete','desoito','desenove','vinte')
nume = int(input('Digite um número entre 0-20: '))
if nume < 0 or nume > 20:
    while True:
        nume = int(input('Tente novamente, Digite um número entre 0-20: '))
        if nume >= 0 and nume <= 20:
            break
print(f'Você digitou o número {num[nume]}')