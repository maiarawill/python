primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar agora?'))
print('Progressão finalizada com {} termos mostrados'.format(total))