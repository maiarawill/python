primeiro = int(input("Digite o primeiro número"))
segundo = int(input("Digite o segundo número"))

if primeiro > segundo:
    print('O primeiro valor é maior')
elif segundo > primeiro:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior')