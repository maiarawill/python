import random
jogador = int(input('Entre 0 e 5, em que número eu estou pensando?'))
sorteio = random.randint(0,5)
if jogador == sorteio:
    print("Você acertou eu pensei no {}".format(sorteio))
else:
    print("Você errou!!! Eu pensei no {}".format(sorteio))
