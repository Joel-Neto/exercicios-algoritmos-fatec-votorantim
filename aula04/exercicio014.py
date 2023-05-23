horasEmValorReal = float(input('Digite as horas: '))
horasEmValorInteiro = round(horasEmValorReal)
quantidadeMinutos = (horasEmValorInteiro * 60) + (100 * (horasEmValorReal - horasEmValorInteiro))

print(f'{horasEmValorReal} horas correspondem a {quantidadeMinutos} minutos!')
