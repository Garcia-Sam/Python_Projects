print('10 TERMOS DE UMA RAZÃO')
pt = int(input('Digite o PRIMEIRO TERMO: '))
raz = int(input('Digite a RAZÃO: '))
decimo = pt + (10 - 1) * raz
for c in range(pt, decimo + raz, raz):
    print(f'{c}', end=', ')
print('FIM.')
