lista = []
listapar = []
listaimpar = []

while True:
    lista.append(int(input('\nDigite um valor: ')))

    escolha = str(input('Quer mais um número? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Resposta inválida...')
        escolha = str(input('Quer adicionar outro? [S/N] ')).strip().upper()[0]

    if escolha == 'N':
        break

for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        listapar.append(lista[i])
    else:
        listaimpar.append(lista[i])

print(f'\nOs valores digitados foram: {lista}')
print(f'Os valores pares da lista são: {listapar}')
print(f'Os valores ímpares da lista são: {listaimpar}')
