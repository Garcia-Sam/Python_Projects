cont = mult = 0
while True:
    num = int(input('Deseja ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('--' * 10)
    for cont in range(1, 11):
        print(f'{num:2} x {cont:2} = {num * cont:2}')
    print('--' * 10)
print('Programa encerrado.')
