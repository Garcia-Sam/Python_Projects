dias = int(input('Quantos dias o carro foi alugado? '))
kim = float(input('Quantos Km foram rodados? '))
v = (dias * 60) + (kim * 0.15)
print(f'Você vai precisar pagar R${v:.2f} de aluguel. ')
