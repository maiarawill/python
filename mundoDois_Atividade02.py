num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases de conversão:
\033[1;34;43m[1] converter para BINÁRIO\033[m
\033[1;32;46m[2] Converter para OCTAL\033[m
\033[1;33;47m[3] Converter para HEXADECIMAL\033[m''')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print('\033[1;34;43m{} convertido para BINÁRIO é igual a {}\033[m'.format(num, bin(num)))
elif opcao == 2:
    print('\033[1;32;46m{} convertido para OCTAL é igual a {}\033[m'.format(num, oct(num)))
elif opcao == 3:
    print('\033[1;33;47m{} convertido para HEXADECIMAL é igual a {}\033[m'.format(num, hex(num)))
else:
    print('\033[1;31;40m Tente novamente \033[m')

