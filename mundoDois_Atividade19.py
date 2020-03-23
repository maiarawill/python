import datetime
atual = datetime.date.today().year
maioridade = 0
menorIdade = 0
for verificador in range (0, 7):
    nascimento = int(input('Qual o seu ano de nascimento?'))
    ano = atual - nascimento
    if ano >= 18:
        maioridade += 1
    else:
        menorIdade +=1
print('{} são maior de idade, {} são menor de idade'.format(maioridade, menorIdade))