reta1 = float(input('Indique um valor para uma reta: '))
reta2 = float(input('Indique outro valor: '))
reta3 = float(input('Indique o último valor: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Você consegue formar um triângulo com esses valores!')
    if reta1 == reta2 == reta3:
        print('Esse triângulo é classificado como: EQUILÁTERO!')
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
        print('Esse triângulo é classificado como: ISÓSCELES!')
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print('Esse triângulo é classificado como: ESCALENO!')
else:
    print('Você não consegue formar um triângulo com esses valores.')
