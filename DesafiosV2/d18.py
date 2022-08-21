frase = str(input('Digite uma frase: ')).strip().isupper()
palavras = frase
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    print(junto[letra])
