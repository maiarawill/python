import datetime
atual = datetime.date.today().year
ano = 0
media = 0
minimo = 20
mulher = 0
name = ''
ano = 0
for c in range(0, 4):
    nome = input('Qual o seu nome?')
    idade = float(input('Qual a sua idade?'))
    sexo = input('qual o seu sexo?[M/F]')
    media += idade
    if sexo == 'm' and idade > ano:
        ano = idade
        name = nome
    if sexo == 'f' and idade < minimo:
        mulher += 1

else:
    print('Não tem homens no grupo')

total = media /4
print('A idade média do grupo é de {}\n'
      'O homem mais velho tem {} anos e se chama {}\n'
      'Ao todo são {} mulheres com menos de 20 anos'.format(total, ano, name, mulher))