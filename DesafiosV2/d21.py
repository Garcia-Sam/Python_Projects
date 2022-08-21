somaidae = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for pessoa in range(1, 5):
    print(f'\033[1m---- {pessoa}ª PESSOA ----\033[m')
    nome = str(input('Nome: ')).strip().isupper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidae += idade

    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1

mediaidade = somaidae / 4
print(f'A média da Idade do grupo é {mediaidade:.2f} ')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
