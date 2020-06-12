from datetime import datetime


def voto(id = 0):
    idade = datetime.now().year - id
    if idade < 16 or idade > 65:
        valor = 'Não vota'
        return idade, valor
    elif idade >= 16 and idade < 18:
        valor = 'Voto Opcional'
        return idade, valor
    elif idade >= 18 or idade < 65:
        valor = 'Voto Obrigatorio'
        return idade, valor


print('-'*40)
ano = int(input('digite seu ano de nascimento: '))
print(f'Com idade {voto(ano)[0]}: {voto(ano)[1]}')
