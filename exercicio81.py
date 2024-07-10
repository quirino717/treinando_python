lista = []

while True:
    lista.append(int(input('\nDigite um valor: ')))

    escolha = str(input('Quer mais um número? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Resposta inválida...')
        escolha = str(input('Quer adicionar outro? [S/N] ')).strip().upper()[0]

    if escolha == 'N':
        break

print(f'\nForam adicionados {len(lista)} números na lista')

lista.sort(reverse=True)
print(f'A lista em ordem decrescente fica assim: {lista}')

print('O número 5 está presente na lista' if 5 in lista else 'O número 5 não está presente na lista')
