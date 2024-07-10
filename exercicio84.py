lista = []
dados = []
pesado = menor = 0

while True:
    dados.append(str(input('\nNome: ')).capitalize().strip())
    dados.append(float(input('Peso: ')))

    if len(lista) == 0:
        pesado = menor = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    lista.append(dados[:])
    dados.clear()

    escolha = str(input('Quer adicionar outra pessoa? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Resposta inválida...')
        escolha = str(input('Quer adicionar outra pessoa? [S/N] ')).strip().upper()[0]

    if escolha == 'N':
        break

print(f'\nO maior peso registrado foi \033[4m{pesado:.2f}Kg\033[m. Quem tem esse peso: ', end='')
for i in lista:
    if i[1] == pesado:
        print(f'\033[1m{i[0]}\033[m', end=', ')

print()

print(f'\nO menor peso registrado foi \033[4m{menor:.2f}Kg\033[m. Quem tem esse peso: ', end='')
for i in lista:
    if i[1] == menor:
        print(f'\033[1m{i[0]}\033[m', end=', ')

print()
