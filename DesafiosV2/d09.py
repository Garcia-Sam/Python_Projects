prec = float(input('Qual o valor do produto? '))
pag = float(input('Indique a forma de pagamento:'
                  ' 1-Dinheiro/Cheque 2-Cartão: '))
if pag == 1:
    print(f'O valor total, como desconto a vista é {prec - (prec * 0.1):.2f}')
if pag == 2:
    div = int(input('1-A vista, 2-Em duas vezes, 3-Em três vezes: '))
if div == 1:
    print(f'O valor total, com o desconto com cartão a vista é de {prec - (prec * 0.05):.2f}')
elif div == 2:
    print(f'O valor total vai ser {prec / 2:.2f} em duas vezes.')
elif div == 3:
    print(f'O valor total, com mais 20% do parcelamento vai ser {prec + (prec * 0.2) / 3:.2f}')
else:
    print('OPÇÃO INVÁLIDA!')
