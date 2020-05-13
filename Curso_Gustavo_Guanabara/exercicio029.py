velocidade = int(input('Digite  a velocidade do seu carro = KM'))

if velocidade > 80:
    multa = (velocidade - 80)*7
    print('Você está acima da velocidade permitada, vai pagar multa')
    print('R$07,00 por km a mais, vc pagara R${:.2f}'.format(multa))
else:
    print('Você está na volocidade permitida')