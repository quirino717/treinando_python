lista = []
contador = num = 0

while True:
    num = (int(input('\nDigite um valor: ')))

    if num in lista:
        print('Esse valor já está na lista!!')
    else:
        lista.append(num)

    escolha = str(input('Quer adicionar outro? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Resposta inválida...')
        escolha = str(input('Quer adicionar outro? [S/N] ')).strip().upper()[0]

    if escolha == 'N':
        break

print(f'\nOs valores digitados foram: {sorted(lista)}')