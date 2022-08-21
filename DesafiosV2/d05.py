nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'\033[34mTirando {nota1} e {nota2}, a média é {media}\033[m')
if media < 5:
    print(f'Sua média foi "{media}".'
          f' \033[31mREPROVADO!\033[m')
elif 7 > media >= 5:
    print(f'Sua média foi "{media}".'
          f' \033[33mRECUPERAÇÃO!\033[m')
elif media >= 7:
    print(f'Parabéns! Sua média foi "{media}". '
          f' \033[32mAPROVADO!\033[m')
