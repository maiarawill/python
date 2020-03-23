peso = float(input("Qual o seu peso?"))
tamanho = float(input('Qual a sua altura?'))

calculo = peso / (tamanho * tamanho)
print('IMC = {}'.format(calculo))
if calculo < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= calculo <= 25:
    print('Você está com o peso ideal')
elif 25 < calculo <= 30:
    print('Você está com sobrepeso')
elif 30 < calculo <= 40:
    print('Você está com obesidade')
elif 40 < calculo <= 60:
    print('Você está com obesidade mórbida')
else:
    print('Números digitados erraddos')