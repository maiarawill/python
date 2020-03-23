numero = int(input('Digite um número'))
contador = 0
for verificador in range(1, numero +1):
    if numero % verificador == 0:
        contador +=1
        print(verificador)
if contador == 2:
            print('É Primo ')
else:
    print('Não é primo')
