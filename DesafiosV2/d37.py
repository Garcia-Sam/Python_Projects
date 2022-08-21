lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
        'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um número entre 0 e 20: '))
if num < 0 or num > 20:
    print('Tente novamente. Digite de 0 a 20: ')
elif num in lista:
    print(f'Seu número escrito por extensso é {lista[num]}.')

print('Olá, mundo')