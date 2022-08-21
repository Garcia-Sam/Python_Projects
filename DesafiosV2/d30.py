respo = 'S'
soma = quant = media = maior = menor = 0
while respo in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    respo = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
media = soma / quant
print(f'Você digitou {quant} e a média foi {media:.2f} .')
print(f'O maior foi {maior} e o menor foi {menor} .')
