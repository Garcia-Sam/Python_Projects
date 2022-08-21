altura = float(input('Indique sua altura: (m) '))
peso = float(input('Indique seu peso: (Kg) '))
imc = peso / (altura ** 2)
print(f'Seu IMC é: {imc:.1f}')
if imc < 18.5:
    print('De acordo com o seu IMC, você esta ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('De acordo com seu IMC, você esta no PESO IDEAL.')
elif 25 <= imc < 30:
    print('De acordo com seu IMC, você esta com SOBREPESO.')
elif 30 <= imc < 40:
    print('De acordo com seu IMC, você esta com OBESIDADE.')
elif imc > 40:
    print('De acordo com seu IMC, você esta com OBESIDADE MÓRBIDA.')
else:
    print('OPÇÃO INVÁLIDA.')
