txt = input('Digite uma frase para verificar a quantidade de palavras: ')
arrayTxt = txt.split()

print(arrayTxt)
print(f'A frase digitada possui {len(arrayTxt)} palavras!')