num1 = float(input('Digite o primero número: '))
num2 = float(input('Digite o segundo número: '))

escolha = input(
    '\n1 - Média entre os números digitados;'
    '\n2 - Diferença do maior pelo menor;'
    '\n3 - Produto entre os números digitados;'
    '\n4 - Divisão do primeiro pelo segundo'
    '\n\nQual das opções você deseja escolher? '
)

if escolha == '1':
    media = (num1 + num2) / 2
    print(f'A media entre {num1} e {num2} é igual a {media}!')
elif escolha == '2':
    if num1 > num2:
        print(f'A diferença entre {num1} e {num2} é igual a {num1 - num2}!')
    elif num2 > num1:
      print(f'A diferença entre {num2} e {num1} é igual a {num2 - num1}!')
    else:
        print('Os números são iguais, portanto, a diferença é igual a 0!')
elif escolha == '3':
    print(f'O produto entre {num1} e {num2} é igual a {num1 * num2}!')
elif escolha == '4':
    print(f'A divisão de {num1} por {num2} é igual a {num1 / num2}!')
else:
    print('Valor inválido!')

