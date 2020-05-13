#022
nome = input('Nome = ')
print(nome.upper())
print(nome.lower())
print('Total de letras(com os espaços)= {}'.format(len(nome)))
print(len(nome.replace(' ','')))
print(nome)
print(nome.replace(' ',''))
nome2 = nome.split()
print(nome2[0])
print(len(nome2[0]))

#023
n = input('digite um número =')
n = n.zfill(4)
n = ' '.join(n)
n = n.split()
print('Unidade {}'.format(n[3]))
print('Dezena {}'.format(n[2]))
print('Centena {}'.format(n[1]))
print('Milha {}'.format(n[0]))

#024
cidade = input('Digite o nome da sua Cidade = ')
cidade = cidade.split()
print(cidade)
print('A cidade começa com Santo? [True = Sim / False = Não] = {}'.format('Santo' in cidade[0]))
if cidade[0].find('Santo') == 0:
    print('A cidade começa com a Palavra Santo')
else:
    print('A cidade não começa com a Palavra Santo')

#025
nome = input('Digite seu nome = ')
nome = nome.capitalize()
print('Existe Silva no nome ? {}'.format('Silva' in nome))