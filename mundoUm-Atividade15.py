km = float(input('Quantos km você percorreu?'))
dias = int(input('QUantos dias você irá ficar?'))

cad = dias * 60
calc = km * 0.15
total = calc + cad

print('Você irá gastar {} por alugar o carro por {} dias e ter rodado {} km'.format(total, dias, km))