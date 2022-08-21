salario = float(input('Qual valor do seu salário? R$'))
sala15 = salario * (15 / 100)
sala10 = salario * (10 / 100)
if salario >= 1250:
    print(f'Seu salário com 10% de aumento será R${sala10 + salario:.2f}')
else:
    print(f'Seu salário com 15% de aumento será R${sala15 + salario:.2f}')
