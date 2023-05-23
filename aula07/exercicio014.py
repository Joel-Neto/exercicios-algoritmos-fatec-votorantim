x = int(input('Digite um valor para calcular seu fatorial: '))
cont, fatorial = 1, 1

while cont <= x:
    fatorial *= cont
    cont += 1

print(f'{x}! = {fatorial}')