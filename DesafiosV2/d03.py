nu1 = int(input('Digite um número inteiro: '))
nu2 = int(input('Digite outro número inteiro: '))
if nu1 > nu2:
    print(f'O número "{nu1}" é o maior.')
elif nu2 > nu1:
    print(f'O número "{nu2}" é o maior.')
elif nu1 < nu2:
    print(f'O número "{nu1}"é o menor.')
elif nu2 < nu1:
    print(f'O número "{nu2}" é o menor.')
elif nu1 == nu2:
    print('Não existe valor maior, os dois são iguais.')
else:
    print('Você quebrou o código. Parabéns!')
