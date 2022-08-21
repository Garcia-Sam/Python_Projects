from datetime import date

ano = int(input('Qual ano queres analisar? (Coloque 0 para analisar o atual) '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Esse ano "{ano}" é BISSEXTO!')
else:
    print(f'Esse ano "{ano}" não é BISSEXTO!')
