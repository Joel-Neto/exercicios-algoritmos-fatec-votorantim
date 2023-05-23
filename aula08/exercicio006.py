txt = input('Digite algo para verificar se é palíndromo: ')
txt = txt.lower()
txtInverso = ''
for i in txt[::-1]:
    txtInverso += i

if (txt == txtInverso):
    print(f'{txt} é PALÍNDROMO!')
else:
    print(f'{txt} não é PALÍNDROMO!')