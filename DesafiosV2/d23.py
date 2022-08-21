# melhorar o jogo do desafio 28. Computador tem que pensar de 0 a 10, até o jogador acertar.
from random import randint
comp = randint(0, 10)
acertou = False
tenta = 0
print('Tente acertar um número de 0 a 10.')
while not acertou:
    jog = int(input('Qual seu palpite? '))
    tenta += 1
    if jog == comp:
        acertou= True
    else:
        if jog < comp:
            print('Mais... Tente novamente: ')
        elif jog > comp:
            print('Menos... tente novamente: ')
print(f'Acertou!! Com {tenta} tentativas.')
