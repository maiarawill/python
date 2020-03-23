maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input('Peso da {}° pesssoa:'.format(p)))
    if p == 1:
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso foi de {}Kg e o menor foi de {}Kg'.format(maior, menor))