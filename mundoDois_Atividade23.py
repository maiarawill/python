from random import randint
computador = randint(0, 10)
acertar = False
palpite = 0
while not acertar:
    jogador = int(input('Qual o seu palpite'))
    palpite += 1
    if jogador == computador:
        acertar = True
    else:
        if jogador < computador:
            print('Mais, tente mais uma vez')
        elif jogador > computador:
            print ('Menos, tente mais uma vez')
print('Acertou com {} tentativas'.format(palpite))
