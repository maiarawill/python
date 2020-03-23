n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
opcao = 0
while opcao != 5:
    print('''    [1]Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('Qual a sua opção?'))
    if opcao == 1:
        soma = n1 + n2
        print ('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicacao = n1 * n2
        print ('A multiplicação entre {} x {} é {}'.format(n1, n2, multiplicacao))
    elif opcao == 3:
        if n1 > n2:
            print ('{} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
    elif opcao == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor valor:'))
    elif opcao == 5:
        print('Finalizado')
    else:
        print('Opção inválida. Tente novamente!')