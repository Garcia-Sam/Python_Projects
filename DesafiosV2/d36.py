# programa que simule um caixa. perguntar qual valor vai ser sacado. programa vai informar quantas cédulas serão entregues 50,20,10,1
valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:  # verifica quantas vezes consegue tirar 50
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'O total é {totced} cédulas de R${ced} reais.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('Volte Sempre!!')
