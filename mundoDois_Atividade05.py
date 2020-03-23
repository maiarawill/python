nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))

media = (nota1 + nota2)/2

if media >= 7:
    print('Parabéns, você foi aprovado com {}'.format(media))
elif 5 <= media < 7:
    print('Você esta em recuperação, sua nota foi {}'.format(media))
elif media < 5:
    print('Você tirou {} e esta reprovado'.format(media))