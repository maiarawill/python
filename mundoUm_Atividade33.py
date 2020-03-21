primeiro = float(input('Digite o primeiro número:'))
segundo = float(input('Digite o segundo número:'))
terceiro = float(input('Digite o terceiro número:'))

if primeiro > segundo and primeiro > terceiro:
    print("{} é maior que {} e {}".format(primeiro,segundo,terceiro))
elif segundo > primeiro and segundo > terceiro:
    print("{} é maior que {} e {}".format(segundo,primeiro,terceiro))
elif terceiro > primeiro and terceiro > segundo:
    print("{} é maior que {} e {}".format(terceiro,primeiro,segundo))
else:
    print("Algo de errado não esta certo, tente novamente! Sugestão: Confira se algum dos números são iguais")
maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

print('O maior número é o: {} e o menor é o {}'.format(maior, menor))
