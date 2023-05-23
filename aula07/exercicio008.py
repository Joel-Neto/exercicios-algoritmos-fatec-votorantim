num = int(input('Digite um número para verificar se é primo: '))
cont = 0
i = 1
for i in range(1, num+1):
    if num % i == 0:
        cont += 1

if cont == 2:
    print(f'{num} é primo!')
else:
    print(f'{num} não é primo!')

# while i <= num:
#     if num % i == 0:
#       cont += 1
#     i += 1

# if cont == 2:
#     print('Primo!')
# else:
#     print('Não é primo!')