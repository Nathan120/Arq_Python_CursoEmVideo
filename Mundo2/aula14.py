sex = ''
while sex != 'M' and sex != 'F':
    sex = str(input('Sexo[M/F] = ')).upper()
    if sex == 'F' or sex == 'M':
        print('Valor inserido {}'.format(sex))
    else:
        print('Valor inválido!')
print('Fim!')
while sex not in 'MmFf':
    print('brabo')