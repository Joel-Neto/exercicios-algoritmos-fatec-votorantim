data = input('Digite uma data (dd/mm/aaaa): ')
dataArray = data.split('/')

print(f'Data no formato (aaaa/mm/dd) => {dataArray[2]}/{dataArray[1]}/{dataArray[0]}')