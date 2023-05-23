n = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
soma, cont = 0, 1 

while cont <= n:
    soma += (b ** cont)
    cont += 1

print(f'O resultado da soma é {soma}!')