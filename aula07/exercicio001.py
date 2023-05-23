num = int(input('Digite um número inteiro e positivo: '))

soma = 0
for i in range(1, num + 1):
  soma += (2 ** i)

print(f'O valor da soma é {soma}!')