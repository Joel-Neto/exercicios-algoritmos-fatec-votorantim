salario = float(input('Digite o seu salário: '))
percentualAumento = float(input('Digite o aumento percentual(%): '))
novoSalario = salario + (salario * (percentualAumento/100))

print(
    f'Sau salário atual é R${salario:.2f} e seu novo salário será R${novoSalario:.2f}'
)