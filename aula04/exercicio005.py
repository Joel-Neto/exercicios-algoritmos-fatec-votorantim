salario = float(input('Digite o seu salário: '))

novoSalario = salario + (salario * (25/100))

print(
    f'Sau salário atual é R${salario:.2f} e seu novo salário será R${novoSalario:.2f}'
)