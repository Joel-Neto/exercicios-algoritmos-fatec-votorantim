base = float(input('Digite o valor da base: '))
altura = float(input('Digite o valor da altura: '))

while ((base <= 0) or (altura <= 0)):
    if ((base <= 0) and (altura > 0)):
        print('O valor da base deve ser maior que zero!')
        base = float(input('Digite o valor da base: '))
    elif ((altura <= 0) and (base > 0)):
        print('O valor da altura deve ser maior que zero!')
        altura = float(input('Digite o valor da altura: '))
    else:
        print('O valor da base e da altura devem ser maiores que zero!')
        base = float(input('Digite o valor da base: '))
        altura = float(input('Digite o valor da altura: '))

area = base * altura / 2

print(f'Um triângulo com base igual a {base} e altura igual a {altura} tem uma área igual a {area:.2f}!')