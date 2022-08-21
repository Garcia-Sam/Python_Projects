from datetime import date
nasci = int(input('Qual o ano do seu nascimento? '))
atual = date.today().year
idade = atual - nasci
data2 = idade - 18
data3 = 18 - idade
print(f'Quem nasceu em {nasci}, tem {idade} anos.')
if atual == 18:
    print('Chegou a hora de se alistar no serviço militar.')
elif atual > 18:
    print('Já passou do tempo de se alistar.')
    print(f'Se passaram "{data2}" anos, desde o seu tempo de alistamento.')
elif atual < 18:
    print('Sua hora de alistar esta chegando mocinho.')
    print(f'Faltam "{data3}" anos até se alistar')
else:
    print('Opção Inválida.')
