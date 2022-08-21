nome = str(input('Digite seu nome completo: ')).strip()
pn = nome.split()
print(f'Seu primeiro nome é {pn[0]}.')
print(f'Seu ultimo nome é {pn[len(pn) - 1]}.')
