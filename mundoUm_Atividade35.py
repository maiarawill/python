b1 = int(input("Digite o valor da primeira reta:"))
b2 = int(input("Digite o valor da primeira reta:"))
b3 = int(input("Digite o valor da primeira reta:"))
if b1 < b2 + b3 and b2 < b3 + b1 and b3 < b1 + b2:
    print("Você consegue fazer um triângulo")
else:
    print('Você não consegue formar um triângulo')