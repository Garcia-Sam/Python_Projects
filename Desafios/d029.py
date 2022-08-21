viag = float(input('Quantos Km tem a sua viagem? '))
if viag < 200.0:
    print(f'Sua viagem vai custar R${viag * 0.50:.2f}')
else:
    print(f'Sua viagem vai custar R${viag * 0.45:.2f}.')
