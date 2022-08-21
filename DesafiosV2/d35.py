# leia nome e preço do produto. perguntar se vai continuar. total gasto. quantos custam mais de 1000 e o nome do produto mais barato
mais1000 = totalgasto = menor = conta = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    prec = float(input('Preço do produto: R$'))
    conta += 1
    totalgasto += prec
    if prec >= 1000:
        mais1000 += 1

    if conta == 1 or prec < menor:
        menor = prec
        barato = nome

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total gasto foi de R${totalgasto:.2f}')
print(f'Temos {mais1000} produtos que custaram mais de R$1.000 reais.')
print(f'O produto mais brato foi {barato} que custa R${menor:.2f} reais.')
