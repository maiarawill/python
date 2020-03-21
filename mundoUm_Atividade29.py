velocidade = int(input('Qual a velocidade do do seu carro?'))
if velocidade >80:
    multa = (velocidade - 80)* 7
    print("Você recebeu uma multa no valor de R${}".format(multa))
else:
    print('Parabéns, você esta dentro das normas de trânsito')