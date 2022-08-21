from math import cos, sin, tan, radians

angu = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angu))
coss = cos(radians(angu))
tang = tan(radians(angu))
print(f'O seno vale {seno:.2f} o cosseno {coss:.2f} e a tangente {tang:.2f}.')
