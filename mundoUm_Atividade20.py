import random
a1 = str(input('Qual o primeiro aluno?'))
a2 = str(input('Qual o segundo aluno?'))
a3 = str(input('Qual o terceiro aluno?'))
a4 = str(input('Qual o quarto aluno?'))

lis = [a1, a2, a3, a4]
random.shuffle(lis)
print('A ordem de apresentação será:')
print(lis)
