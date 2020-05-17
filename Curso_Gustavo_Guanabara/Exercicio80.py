ista = []
for i in range(0,5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > ista[-1]:
        ista.append(num)
    else:
        pos = 0
        while pos < len(ista):
            if num <= ista[pos]:
                ista.insert(pos, num)
                break
            pos += 1
print(ista)

