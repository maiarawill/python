from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
escolha = int(input('Qual número você escolhe?'))
if computador == 0:
    if escolha == 0:
        print('EMPATE')
    elif escolha == 1:
        print('Você VENCEU')
    elif escolha == 2:
        print('Você PERDEU')
    else:
        print('Jogada inválida')
elif computador == 1:
    if escolha == 0:
        print('Você PERDEU')
    elif escolha == 1:
        print('EMPATE')
    elif escolha == 2:
        print('Você VENCEU')
    else:
        print('Jogada inválida')
elif computador == 2:
    if escolha == 0:
        print('Você VENCEU')
    elif escolha == 1:
        print('Você PERDEU')
    elif escolha == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')

print('Você jogou {} e o computador jogou {}'.format(itens[escolha], itens[computador]))
