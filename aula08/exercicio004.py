txt = input('Digite uma frase ou uma palavra: ')
contVogais = 0

for i in txt:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        contVogais += 1

print(f'A frase / palavra: "{txt}" possui {contVogais} vogais!')