valor = float(input('Quanto você gastou nas compras?'))

print('[1]Dinheiro ou cheque \n'
      '[2]Cartão de débito \n'
      '[2]Cartão de débito \n'
      '[3]2x no cartão \n'
      '[4]3x ou mais')
escolha = int(input('Qual a forma de pagamento?'))
desconto = 0
if escolha == 1:
    desconto = (valor * 90)/100
elif escolha == 2:
    desconto = (valor * 95) / 100
elif escolha == 3:
    desconto = (valor * 98) / 100
elif escolha == 4:
    desconto = (valor * 1.20)
else:
    print("Escolha indisponivel")
print("Você ira pagar no total: {}".format(desconto))

