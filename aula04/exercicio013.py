valorSalario = float(input('Digite o valor do salário mínimo: R$'))
quantidadeQuilowatt = int(input('Digite a quantidade de quilowatt: '))

valorQuilowatt = valorSalario / 8

valorQuilowattResidencia = quantidadeQuilowatt * valorQuilowatt

print(f'O valor de cada quilowatt é igual a R${valorQuilowatt:.2f}')
print(f'Você utilizou {quantidadeQuilowatt} quilowatts, portanto, deverá pagar R${valorQuilowattResidencia:.2f}')
print(f'Com 15% de desconto, o preço será de {valorQuilowattResidencia - (valorQuilowattResidencia * 0.15)}')