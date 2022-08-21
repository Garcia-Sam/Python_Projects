sex = str(input('Indique seu gênero [M/F]: ')).upper().strip()[0]
while sex not in 'MmFf':
    sex = str(input('Incorreto, tente novamente: ')).upper().strip()[0]
print('Dado Registrado.')
