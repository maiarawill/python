import math
co = float(input('Qual o cateto oposto?'))
ca = float(input('Qual o cateto adjacente?'))

hip = (co * co) + (ca * ca)
cal = math.sqrt(hip)

print('A hipotenusa é igual a : {}'.format(cal))