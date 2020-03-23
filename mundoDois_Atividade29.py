num = 0
contador = 0
soma = 0
num = int(input('Digite um número [999 para parar]'))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número [999 para parar]'))
print('Você digitou {} números e a soma entre eles foi {}.'.format(contador, soma))