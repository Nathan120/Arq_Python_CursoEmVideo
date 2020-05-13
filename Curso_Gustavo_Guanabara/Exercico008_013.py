valor = float(input('Digite a medida em metros = '))
cemt = valor * 100
mili = valor * 1000
print('metros {} \n centimetros {} \n milimetros {}'.format(valor,cemt,mili))

altura = float(input('Digite a altura da parede = '))
largura = float(input('Digite a largura da parede = '))

area = (altura * largura)/2
tinta = area/2
print('A área total é = {:.2f}, então é necessário {:.2f} litros de tinta para pintar essa parede'.format(area,tinta))

preço = float(input('Digite o preço do produto = R$'))
desconto = (preço * 5)/100
print('O produto agora está por {:.2f} com 5% de desconto'.format(preço - desconto))

salario = float(input('Digite seu salário = '))
aumento = (salario * 15)/100
print('Seu novo salário é {:.2f}'.format(salario+aumento))