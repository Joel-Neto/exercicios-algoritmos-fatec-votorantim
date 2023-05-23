while True:
    m = float(input('Digite um número: '))
    n = float(input('Digite outro número: '))
    soma = m + n
    print(f'{m} + {n} = {soma}')
    if m > n:
        print(f'M = {m} é maior que N = {n}')
    elif n > m:
        print(f'N = {n} é maior que M = {m}')
    else:
        print(f'M = {m} é igual a N = {n}')

    escolha = input('Deseja continuar (s / n)? ')
    if escolha == 'n':
        print('Saindo da aplicação! ')
        break
    