idade = int(input('\nDigite a sua idade: '))

print('\nSua categoria é:')
if idade > 30:
    print('Sênior!')
elif idade >= 16 and idade <= 30:
    print('Adulto!')
elif idade >= 11 and idade <= 15:
    print('Adolescente!')
elif idade >= 8 and idade <= 10:
    print('Juvenil!')
elif idade >= 5 and idade <= 7:
    print('Infantil!')
else:
    print('Muito jovem! Deve esperar até os 5 anos!')