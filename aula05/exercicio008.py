precoLiquido = float(input('Digite o preço líquido de um produto: R$'))
procedencia = input(
    '1 - SUL\n2 - NORTE\n3 - NORDESTE\n4 - CENTRO-OESTE\n5 - SUDESTE'
    '\nQual é a procedência do produto? '
)
valorImposto = 0
local  = ''

if procedencia == '1':
    valorImposto = 0.11
    local = 'SUL'
elif procedencia == '2':
    valorImposto = 0.13
    local = 'NORTE'
elif procedencia == '3':
    valorImposto = 0.09
    local = 'NORDESTE'
elif procedencia == '4':
    valorImposto = 0.12
    local = 'CENTRO-OESTE'
elif procedencia == '5':
    valorImposto = 0.18
    local = 'SUDESTE'
else:
    print('Valor inválido!')

imposto = precoLiquido + (precoLiquido * valorImposto)
print(f'O produto tem como procedência o {local}, portanto, seu valor com um imposto de {valorImposto * 100}% será de R${imposto:.2f}')

