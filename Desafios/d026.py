from random import choice

numero = int(input('Entre 0 e 5, em qual número eu estou pensando? '))
n = [0, 1, 2, 3, 4, 5]
resposta = choice(n)
if numero == resposta:
    print('Parabéns!! Você acertou!')
else:
    print(f'Que pena, eu pensei no {resposta} o computador venceu!')
