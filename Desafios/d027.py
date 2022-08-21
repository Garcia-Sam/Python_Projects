velo = float(input('Qual a velocidade em que você estava? '))
if velo > 80:
    print('Você foi multado!')
    print(f'O valor da sua multa é de R${(velo - 80) * 7:.2f}. Você excedeu o limite de 80Km/h.')
else:
    print('Parabéns! Nada de multa pra você!')
