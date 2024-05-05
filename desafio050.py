numeros = []
for i in range(1, 7):
    inteiro = (int(input(f'Digite o {i}º número inteiro: ')))
    if inteiro % 2 == 0:
        numeros.append(inteiro)

print(sum(numeros))
