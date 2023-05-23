a, b = 0, 1
cont = 3
print(f'{a} - {b} ', end='')

while cont <= 10:
  c = a + b
  a = b
  b = c
  print(f'- {c} ', end='')
  cont += 1
