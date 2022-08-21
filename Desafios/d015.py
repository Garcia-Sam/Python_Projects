#import math
from math import hypot

oposto = float(input('Qual o comprimento do cateto oposto? '))
adja = float(input('Qaual o comprimento do cateto adjacente? '))
hipo = hypot(oposto, adja)
print(f'A hipotenusa vai medir {hipo:.2f}')
