prim = int(input('Digite o primeiro termo da razão: '))
raz = int(input('Digite a razão da PA: '))
termo = prim
contador = 1
while contador <= 10:
    print(f'{termo} →', end=' ')
    termo += raz
    contador += 1
print('Fim')
