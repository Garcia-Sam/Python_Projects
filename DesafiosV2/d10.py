from random import randint
from time import sleep
jog = int(input('''\033[1;36mEscolha um para jogar: 
[0]Pedra, [1]Papel, [2]Tesoura: \033[m'''))
print('\033[1;35m-=-\033[m' * 2)
print('\033[1;35m JO\033[m')
sleep(1)
print('\033[1;35m KEN\033[m')
sleep(1)
print('\033[1;35m PO\033[m')
print('\033[1;35m-=-\033[m' * 2)
sleep(1)
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print(f'\033[36mO computador jogou {itens[comp]}.')
print(f'O jogador jogou {itens[jog]}.\033[m')
if comp == 0:  # Computador jogou PEDRA
    if jog == 0:
        print('Deu Empate!')
    elif jog == 1:
        print('Jogador Vence!!')
    elif jog == 2:
        print('Computador Vence!!')
    else:
        print('JOGADA INVÁLIDA!!')
elif comp == 1:  # computador jogou PAPEL
    if jog == 0:
        print('Computador Vence!!')
    elif jog == 1:
        print('Deu Empate!!')
    elif jog == 2:
        print('Jogador Vence!!')
    else:
        print('JOGADA INVÁLIDA!!')
elif comp == 2:  # Computador jogou TESOURA
    if jog == 0:
        print('Jogador Vence!!')
    elif jog == 1:
        print('Computador Vence!!')
    elif jog == 2:
        print('Deu Empate!!')
    else:
        print('JOGADA INVÁLIDA!!')
