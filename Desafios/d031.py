a = int(input('Digite um número: '))
b = int(input('Digite outro: '))
c = int(input('Digite o último: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O seu maior valor foi {maior}.')
print(f'O seu menor valor foi {menor}.')
