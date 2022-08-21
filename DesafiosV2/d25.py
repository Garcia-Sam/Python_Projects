num = int(input('Indique um número para ter seu fatorial: '))
f = num
c = num
while c != 1:
    c -= 1
    f *= c
    print(f'{c}', end=' ')
    print(f' x ' if c > 1 else ' = ', end=' ')
print(f'{f}')
