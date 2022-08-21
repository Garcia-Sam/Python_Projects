nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito, Gustavo!')
elif nome == 'Paulo' or nome == 'Maria' or 'João':
    print('Seu nome é bem popular no Brasil mano.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Nomezão feminino bom em!')
else:
    print('Seu nome é bem normal mano.')
print(f'Tenha um bom dia, {nome}!')
