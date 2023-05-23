valoresImc = []
contPessoas, somaPesos, somaAltura = 1, 0, 0

while contPessoas <= 3:
    peso = float(input(f'Digite o peso da {contPessoas}ª pessoa: '))
    altura = float(input(f'Digite a altura da {contPessoas}ª pessoa: '))
    print('='*40, end=''); print('')
    imc = peso / (altura * altura)
    somaPesos += peso
    somaAltura += altura
    valoresImc.append(imc)
    contPessoas += 1


valoresImc.sort()
mediaPeso = somaPesos / (contPessoas - 1)
mediaAltura = somaAltura / (contPessoas - 1)
print(f'Peso médio: {mediaPeso:.2f} Kgs')
print(f'Altura média: {mediaAltura:.2f} metros')
print(f'Maior IMC: {valoresImc[-1]:.2f}')
print(f'Menor IMC: {valoresImc[0]:.2f}')