altura = float(input('Digite a sua altura (metros): '))
sexo = input('Digite o seu sexo (M / F): ')

if sexo.upper() == 'M':
    pesoIdeal = (72.7 * altura) - 58
else: 
    pesoIdeal = (62.1 * altura) - 44.7

print(f'O seu peso ideal é de {pesoIdeal:.2f} Kgs!')