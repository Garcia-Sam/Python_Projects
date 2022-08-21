print('\033[35m-=\033[m' * 15)
print('\033[36m...ANALISADOR DE TRIÂNGULOS...\033[m')
print('\033[35m-=\033[m' * 15)
reta = float(input('Indique um valor pra uma reta: '))
reta2 = float(input('Indique outro valor: '))
reta3 = float(input('Indique o último valor: '))
if reta < reta2 + reta3 and reta2 < reta + reta3 and reta3 < reta2 + reta:
    print('Você consegue sim fazer um triângulo com essas retas! ')
else:
    print('\033[1;31mVocê não consegue fazer um triângulo. BURRÃO DO CARALHO!!!!!!!!!\033[m')
