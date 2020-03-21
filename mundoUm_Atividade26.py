fra = str(input('Digite uma frase'))
espa = fra.strip()
minu = espa.lower()

print('A letra A aparece {} na frase'.format(minu.count('a')))
print('A primeira letra A aparece na posição {}'.format(minu.find('a')))
print('A última letra A aparece na posição{}'.format(minu.rfind('a')))