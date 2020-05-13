preco = float(input('Digite o preço do produto = R$'))
print("""Escolha a forma de pagamento
        [1] À vista
        [2] À vista(Cartão)
        [3] Até 2X no Cartão
        [4] 3x ou mais no Cartão""")
op = int(input(': '))
if op == 1:
    preco = preco - (preco * (10/100))
    print('O preço final a ser pago é = R${:.2f}'.format(preco))
elif op == 2:
    preco = preco - (preco * (5/100))
    print('O preço final a ser pago é = R${:.2f}'.format(preco))
elif op == 3:
    print('O preço final a ser pago é = R${:.2f}'.format(preco))
elif op == 4:
    preco = (preco * (20/100)) + preco
    print('O preço final a ser pago é = R${:.2f}'.format(preco))
else:
    print('\033[4;33;41mOpção inválida!\033[m')