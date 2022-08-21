numb = int(input('Escreva um número inteiro: '))
conv = int(input('Escolha uma conversão 1-Binário, 2-Octal, 3-Hexadecimal: '))
if conv == 1:
    print(f'Convertendo {numb} para BINÁRIO da {bin(numb)[2:]}')
    print('Muito legal, né?')
elif conv == 2:
    print(f'Convertendo {numb} para OCTAL da {oct(numb)[2:]}')
    print('Muito legal, né?')
elif conv == 3:
    print(f'Convertendo {numb} para HEXADECIMAL da {hex(numb)[2:]}')
    print('Muito legal, né?')
else:
    print('Opção Inválida.')
