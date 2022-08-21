num = int(input('Digite um número para ver sua tabuada: '))
print('=' * 13)
for c in range(1, 11):
    print(f'{num:2} x {c:2} = {num * c:2}')
print('=' * 13)
