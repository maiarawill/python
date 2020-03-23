ano = int(input('Qual o seu ano de nascimento?'))
idade = 2020 - ano

if idade < 18:
    tempo = 18 - idade
    print('Ainda falta {} anos para você se alistar'.format(tempo))
elif idade == 18:
    print('Esta na hora de se alistar')
else:
    tempo = idade -18
    print('Você deveria ter se alistado a {} anos atrás'.format(tempo))