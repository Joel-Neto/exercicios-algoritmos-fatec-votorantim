a = 0
b = 1

print(f'- {a} - {b} - ', end='')
for i in range(1, 11):
    c = a + b
    a = b
    b = c
    print(f'{c} - ', end='')