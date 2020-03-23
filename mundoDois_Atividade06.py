import datetime
atual = datetime.date.today().year
nascimento = int(input('Qual o seu ano de nascimento'))

idade = atual - nascimento


if idade <= 9:
    print('O atleta tem {} anos e esta na categoria: Mirim'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem {} anos e esta na categoria: Infantil'.format(idade))
elif 15 <= idade <= 19:
    print('O atleta tem {} anos e esta na categoria: Junior'.format(idade))
elif 20 <= idade <= 25:
    print('O atleta tem {} anos e esta na categoria: Sênior'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos e esta na categoria: Master'.format(idade))