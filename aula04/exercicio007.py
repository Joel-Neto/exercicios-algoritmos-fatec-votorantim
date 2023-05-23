deposito = float(input('Depósito: R$'))
juros = float(input('Juros: '))

saldo = deposito + (deposito * (juros/100))
juros = deposito * (juros / 100)

print(f'Seu investimento rendeu R${juros:.2f}, portanto seu depósito é de R${deposito:.2f}')