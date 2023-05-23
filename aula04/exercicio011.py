medidaEmPes = float(input('Digite um valor em pés: '))

polegadas = medidaEmPes * 12
jardas = medidaEmPes / 3
milha = jardas / 1760

print(f'Valor em Polegadas = {polegadas}')
print(f'Valor em Jardas = {jardas:.2f}')
print(f'Valor em Milhas = {milha:.5f}')