num = int(input('Digite um número: '))
fatorial = 1
string = ''

for i in range(1, num+1):
  fatorial *= i

for x in range(1, num):
  string += f'{x} * '

print(f'{string}{i} ou {num}! = 120')