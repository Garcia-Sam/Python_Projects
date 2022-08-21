num1 = int(input('Indique o primeiro valor: '))
num2 = int(input('Indique o segundo valor: '))
ent = 0
while ent != 5:
    print('-=-' * 9)
    esco = int(input('Selecione a ação desejada '
                     '\n[1]Somar '
                     '\n[2]Multiplicar '
                     '\n[3]Maior'
                     '\n[4]Novos números'
                     '\n[5]Sair do rograma: '))
    if esco == 1:
        print(f'A soma dos dois valores foi {num1+num2} .')

    elif esco == 2:
        print(f'O resultado da multiplicação é {num1 * num2} .')

    elif esco == 3:
        if num1 > num2:
            print(f'O maior é {num1}.')
        elif num1 == num2:
            print('Não existe mairo maior.')
        else:
            print(f'O mairo é {num2}.')

    elif esco == 4:
        print('-=-' * 9)
        num1 = int(input('Indique um novo valor: '))
        num2 = int(input('Indique outro valor: '))

    elif esco == 5:
        print('ACABOU! SAI DAQUI!')
        break
    else:
        print('Sério?!')
