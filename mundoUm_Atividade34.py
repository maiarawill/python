salario = float(input('Qual o seu salário?'))

if salario >= 1250 :
    aumento = 1.10 * salario
    print("Esse é o seu aumento: R${}".format(aumento))
else:
    aumento = 1.15 * salario
    print("Esse é o seu aumento: R${}".format(aumento))