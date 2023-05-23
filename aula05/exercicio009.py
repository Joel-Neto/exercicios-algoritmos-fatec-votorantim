x = float(input('digite o valor do primero lado do triângulo: '))
y = float(input('digite o valor do segundo lado do triângulo: '))
z = float(input('digite o valor do terceiro lado do triângulo: '))

if ((x + y > z) and (x + z > y) and (y + z > x)):
    print('O comprimento dos lados mencionados forma um triângulo!')
    if ((x == y) and (x == z)):
        print('O triângulo possui os três lados iguais, portanto, é um triângulo equilátero!')
    elif ((x == y) or (y == z) or (x == z)):
        print('O triângulo apresenta apenas dois lados iguais, portanto, é um triangulo isósceles!')
    else:
        print('Todos os lados são diferentes, portanto, é um triângulo escaleno!')    

else:
    print('Não é um triângulo!')