prim = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão da PA: '))
termo = prim
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} →', end=' ')
        termo += raz
        cont += 1
    print('Pausa')
    mais = int(input('Deseja mostrar quantos termo a mais? '))
print(f'Progressão finalizada com {total} termos')
