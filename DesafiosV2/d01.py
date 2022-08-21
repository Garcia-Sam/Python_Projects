print('***' * 10)
print(' Simulador de Financiamento')
print('***' * 10)
casa = float(input('Qual o valor do imóvel desejado? R$'))
salario = float(input('Quanto você recebe por mês? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))
prestacao = casa / (anos * 12)
teto = (salario * 0.3)
if prestacao >= teto:
    print('Sua prestação excedeu o limite de 30% do seu salário.')
    print('Seu empréstimo foi negado! POBRE DO CARALHO!!!!!')
elif prestacao <= teto:
    print('Sua prestação não exceudeu o limite de 30% do seu salário.')
    print('Seu empréstimo foi aprovado!')
else:
    print('Opção invalida.')
