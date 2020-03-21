viagem = float(input("Qual a distância da sua viagem"))
if viagem <= 200:
    valor = viagem * 0.50
    print("Sua viagem irá custar R${}".format(valor))
else:
    valor = viagem * 0.45
    print("Sua viagem irá custar R${}".format(valor))