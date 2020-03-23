frase = str(input('Digite uma frase:'))
palavras = frase.split()
juntar = ''.join(palavras)
verificar = ''
for polindromo in range(len(juntar) - 1, -1, -1):
    verificar += juntar[polindromo]

print('É um polindromo' if verificar == juntar else 'Não é um polindromo')