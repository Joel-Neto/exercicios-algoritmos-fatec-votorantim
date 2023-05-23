valoresImc = []
somaPeso, somaAltura, imc = 0, 0, 0

for i in range(1, 4):
  peso = float(input(f'Digite o peso da {i}ª pessoa: '))
  altura = float(input(f'Digite a altura da {i}ª pessoa (metros): '))
  somaPeso += peso
  somaAltura += altura
  imc = peso / (altura * altura)
  print(f'O IMC da {i}ª pessoa é igual a {imc:.2f}')
  print('=' * 50, end=''); print('')
  valoresImc.append(imc)

pesoMedio = somaPeso / i
alturaMedia = somaAltura / i
valoresImc.sort()

print(f'O peso médio é igual a {pesoMedio:.2f} Kgs!')
print(f'A altura média é igual a {alturaMedia:.2f} metros!')
print(f'O maior IMC é {valoresImc[-1]:.2f} e o menor IMC é {valoresImc[0]:.2f}')
