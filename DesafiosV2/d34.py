# leia a idade e o sexo, perguntar se quer continuar ou não, mostrar maiores de 18/ quantos homens/ quantas mulheres tem menos de 20
mulheres20 = maiores18 = homens = 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'MF': # filtro de limitação
        sexo = str(input('Indique seu gênero [M/F]: ')).strip().upper()[0]
    esc = ' '
    while esc not in 'SN': # filtro para limitação
        esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]

    if esc in 'Nn':
        break

    if sexo == 'F' and idade < 20:
        mulheres20 += 1

    if sexo == 'M':
        homens += 1

    if idade >= 18:
        maiores18 += 1

print(f'{maiores18} pessoas, são maiores de idade.')
print(f'{homens} pessoas, são homens.')
print(f'{mulheres20} pessoas, são mulheres com menos de 20 anos.')