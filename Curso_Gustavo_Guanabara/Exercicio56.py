tid = 0
idvelho = 0
nomevelho = ''
mulnova= 0
for i in range(1, 5):
    print('------\033[4:31m{}ª Pessoa\033[m-------'.format(i))
    nome = str(input('Nome = '))
    idade = int(input('Idade= '))
    sexo = str(input('Sexo [M/F] = '))
    tid += idade
    if i == 1 and sexo in 'Mm':
        idvelho = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > idvelho:
        idvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        mulnova += 1
medid = tid / 4
print('A media de idade é \033[7m{}\033[m'.format(medid))
print('O homem mais velho é {} que tem {} anos'.format(nomevelho,idvelho))
print('Tendo {} mulheres com idade menor que 20 anos'.format(mulnova))