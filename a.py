# Sorteio dos azarados Não consegui entender a sintaxe os diferentes pythons me quebraram nessa
# importa Biblioteca
from random import sample
#Limitando os randons

aluno1 = input('Nome do 1º aluno: ')
aluno2 = input('Nome do 2º aluno: ')
aluno3 = input('Nome do 3º aluno: ')
aluno4 = input('Nome do 4º aluno: ')

list1 = [1, 2, 3, 4]
# random = sample(list1,1) Não se pode usar o random
# Pois a mesma palavra está sendo usada para a biblioteca.
resultadoSorteio = sample(list1, 1) # Vai sortear um número para decidir qual aluno será escolhido.
# if (random ==1)
# escolhido = aluno1
# elif (random ==2)
# escolhido = aluno2
# elif (random ==3)
# escolhido = aluno3
# elif (random ==4)
# escolhido = aluno4

print('O aluno {0} apagará o quadro'.format())