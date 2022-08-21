# leia números inteiros, parar quando digitar 999 desconsiderando ele.
cont = soma = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos valores foi de {soma} e {cont} valores foram digitados.')
