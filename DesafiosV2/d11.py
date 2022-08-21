from time import sleep
print('Contagem regressiva para os fogos:')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
sleep(0.5)
print('HORA DOS FOGOS!!')
