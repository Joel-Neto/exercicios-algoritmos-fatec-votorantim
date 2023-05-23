anoNascimento = int(input('Digite o seu ano de nascimento: '))

idade = 2023 - anoNascimento 
idadeMeses = idade * 12
idadeDias = idade * 365
idadeSemanas = idade * 52

print(
    f'Sua Idade em anos é {idade}\n'
    f'Sua Idade em meses é {idadeMeses}\n'
    f'Sua Idade em semanas é {idadeSemanas}\n'
    f'Sua Idade em dias é {idadeDias}'
)