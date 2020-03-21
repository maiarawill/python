ano = int(input("Qual o ano atual"))
teste1 = ano % 4
teste2 = ano % 100

if teste1 == 0 & teste2 != 0  :
    print("Você esta em um ano bissexto!!!")
else:
    print("Você não esta em um ano bissexto")