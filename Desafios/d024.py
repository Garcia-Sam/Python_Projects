nome = str(input('Digite uma frase: ')).upper().strip()
print(f'Aparece a letra A {nome.count("A")} vezes.')
print(f'A primeira letra A apareceu na posição {nome.find("A") + 1}.')
print(f'A ultima letra A apareceu na posição {nome.rfind("A") + 1}.')
