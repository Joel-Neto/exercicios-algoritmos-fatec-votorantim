somaNumerosPares = 0
cont = 0

while True:
    num = int(input('Digite um número par: '))
    if num == 0:
        print('Encerrando aplicação...')
        break
    if num % 2 != 0:
        print('O número digitado é ímpar, esse valor não será adicionado na soma!')
        continue
    else:
        somaNumerosPares += num
        cont += 1

media = somaNumerosPares / cont
print(f'A média aritmética dos números pares digitados é igual a {media}')