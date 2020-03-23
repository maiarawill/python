resposta = 's'
soma = 0
quantidade = 0
media = 0
maior = 0
menor = 0
numero = 0
while resposta in 'Ss':
    numero = int(input('Digite um número'))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N]')).lower()
media = soma / quantidade
print('Você digitou {} números e a média foi {}'.format(quantidade, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))