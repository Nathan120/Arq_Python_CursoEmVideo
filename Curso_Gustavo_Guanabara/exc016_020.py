''' 0016'''
from math import trunc
n1 = float(input('Digite um número com virgula = '))
print('A parte inteira do número {} é {}'.format(n1,trunc(n1)))

'''0017'''
from math import hypot
co = float(input('Cat Op = '))
ca = float(input('Cat Ad = '))
hip = hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hip))

'''0018'''
from math import cos, sin, tan, radians
ang = float(input('Digite o valor do angulo = '))
print('O sen = {:.2f} \n cos = {:.2f} \n tang = {:.2f}'.format(sin(radians(ang)),cos(radians(ang)),tan(radians(ang))))

'''0019'''
import random
n1 = input('Nome = ')
n2 = input('Nome = ')
n3 = input('Nome = ')
n4 = input('Nome = ')
lista = [n1,n2,n3,n4]
escolha = random.choice
print('O escolhido é = {}'.format(escolha))

'''0020'''