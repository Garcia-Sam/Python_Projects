from random import randint
vitoria = 0
while True:
    jog = int(input('Diga um valor: '))
    comp = randint(0, 10)
    soma = jog + comp
    tipo = ''
    while tipo in 'PI':
        tipo = str(input('Quer PAR ou ÍMPAR [P/I]? ')).strip().upper()[0]
        break
    print(f'Você jogou {jog} e o computador {comp}. Total de {soma}')

    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!!')
            vitoria += 1
        else:
            print('Você PERDEU!!')
            break

    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!!')
            vitoria += 1
        else:
            print('Você PERDEU!!')
            break
        print('Vamos jogar novamente...')
print(f'Você venceu {vitoria} vezes.')
