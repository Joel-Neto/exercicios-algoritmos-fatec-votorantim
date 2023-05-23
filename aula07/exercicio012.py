cont, somaIdades = 0, 0
while True:
    idade = int(input('Digite uma idade: '))
    if idade <= 0:
        print('Encerrando aplicação!')
        break
    else:
      somaIdades += idade
      cont += 1

media = somaIdades / cont
print(f'A média das idades é igual a {media:.2f}, e o número total de pessoas é igual {cont}')