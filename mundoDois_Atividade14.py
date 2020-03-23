num = int(input('Digite um número para ver a sua tabuada:'))
for c in range(1, 11):
    calculo = c * num
    print('{} x {} = {}'.format(num, c, calculo))