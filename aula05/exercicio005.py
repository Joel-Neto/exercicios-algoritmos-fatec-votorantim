anoNascimento = int(input('Digite o seu ano de nascimento: '))
idade = 2023 - anoNascimento
print(f'Sua idade é de {idade} anos!')

if idade >= 18:
    print('Você pode votar e tirar a carteira de habilitação!')

elif idade >= 16 and idade < 18:
    print('Você já pode votar, mas ainda não pode tirar a Carteira de Habilitação!')

else:
    print('Você não pode votar e não pode tirar a Carteira de Habilitação!')