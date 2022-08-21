# tempo = int(input('Quantos anos tem seu carro? '))
# if tempo <= 3:
#    print('Carro novo.')
# else:
#    print('Carro velho.')
# print('Fim.')
# print('Carro novo.' if tempo <= 3 else 'Carro velho.')
# print('Acabou!')

# nome = str(input('Qual seu nome? '))
# if nome == 'Gustavo':
#    print('Que belo nome você tem!')
# else:
#    print('Seu nome é tão normal.')
# print(f'Bom dia {nome}!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média é {m:.1f}.')
if m >= 6.0:
    print(f'Você esta na média {m:.1f}.')
else:
    print('Você não alcançou a média .')
