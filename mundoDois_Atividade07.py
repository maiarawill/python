r1 = float(input('Digite a primeira reta'))
r2 = float(input('Digite a segunda reta'))
r3 = float(input('Digite a terceira reta'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Você pode formar um triângulo e ele será:')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Você não pode formar um triângulo!')