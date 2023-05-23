num = int(input('Digite um número para verificar se este é primo: '))
i, cont = 1, 0

while i <= num:
    if num % i == 0:
        cont += 1
    i += 1

if cont == 2:
    print(f'{num} é PRIMO!')
else: 
    print(f'{num} não é PRIMO!') 
      