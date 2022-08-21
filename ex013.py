# Variáveis Compostas (Tuplas[São imutáveis])
'''lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)'''

'''lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:])'''

'''lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}.', end=' ')
print('\nComi muito!')'''

'''lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(lanche[cont])'''

'''lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}. \nNa posição {cont}')'''

'''lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}. \nNa posição "{pos}".')
print('\nComi muito!')'''

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') #Ordem
print(sorted(lanche))

'''a = (2, 5, 4) # Junção de Tuplas
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))'''

'''a = (2, 5, 4) # Contador de objetos 
b = (5, 8, 1, 2)
c = a + b
print(c.count(9))'''

'''a = (2, 5, 4) # localizador de objeto
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(2, 4))'''

'''pessoas = ('Gustavo', 35, 99.80)
# del(pessoas) # apagar
print(pessoas)'''
