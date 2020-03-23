valor = 0
contador = 0
for c in range(1, 7):
    num = int(input('Digite um {} valor'.format(c)))
    if num % 2 == 0:
        valor = valor + num
        contador +=1
print(valor)