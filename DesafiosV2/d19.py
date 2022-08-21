from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nascimento = int(input(f'Em qual ano a {pessoa}° pessoa nasceu? '))
    idade = (atual - nascimento)
    if idade >= 21:
        totalmaior += 1
    else:
        totalmaior += 1
print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade.')
print(f'Ao todo temos {totalmenor} pessoas menores de idade.')
