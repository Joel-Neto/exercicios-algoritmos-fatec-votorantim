soma = 0
for i in range(1,4):
    nota = float(input(f'Digite a {i}ª nota: '))
    while nota < 0 or nota > 10:
        nota = float(input('ERRO! Digite uma nota entre 0 e 10: '))
    soma += nota

media = soma / i
print(f'\nSua Média é de {media:.2f} pontos!')

if media < 3:
    print('Reprovado!')
elif media >= 3 and media < 7:
    print('Exame!')
    novaNota = 12 - media
    print(f'Você precisa tirar, no mínimo, {novaNota:.2f} pontos!')

    exame = float(input('Digite a nota do EXAME: '))
    while exame < 0 or exame > 10:
        exame = float(input('ERRO! Digite uma nota entre 0 e 10: '))

    novaMedia = (media + exame)/2
    print(f'Sua nova média é {novaMedia:.2} pontos!')
    if novaMedia < 6:
        print('Reprovado!')
    else:
        print('Aprovado!')
else:
    print('Aprovado!')

