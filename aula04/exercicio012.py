alturaDegrau = int(input('Digite a altura de cada degrau: '))
alturaTotal = int(input('Digite a altura que voce deseja subir(m): '))

alturaTotal = alturaTotal * 100

quantidadeDegraus = alturaTotal / alturaDegrau

print(f'Você deverá subir {quantidadeDegraus} degraus!')
