num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if (num1 > num2):
    print(f'{num2} é menor que {num1}')
elif (num2 > num1):
    print(f'{num1} é menor que {num2}')
else:
    print('Os números são iguas!')