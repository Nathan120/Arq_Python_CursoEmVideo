expr = str(input('Digite a expressão: '))
pilha = list()
for c in expr:
    if c == '(':
        pilha.append('(')
    else:
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Tudo certo')
else:
    print('Vou ai que tá errado')