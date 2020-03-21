print('\033[1;31;43m Programa Para Aprovação De Crédito \033[m')
casa = float(input("Qual o valor da casa?"))
salario = float(input("Qual o seu salário?"))
ano = float(input("Em quantas anos você quer parcelar?"))

prestacao = ano * 12
calculo = casa /prestacao
valor = (salario * 30)/100

if calculo > valor:
    print('\033[1;31;40m Seu empréstimo não foi aprovado \033[m')
    print('Para pagar uma cada de R${} em {} anos a prestação será de R${}'.format(casa, ano, calculo))
else:
    print('\033[1;32;40m Seu empréstimo foi aprovado \033[m')
    print('Para pagar uma cada de R${} em {} anos a prestação será de R${}'.format(casa, ano, calculo))