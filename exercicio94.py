from time import sleep
lista = []
dicionario = {}
soma = media = 0

while True:
    dicionario['Nome'] = str(input('\nNome: ')).title().strip()
    dicionario['Idade'] = int(input('Idade: '))
    while True:
        dicionario['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dicionario['Sexo'] in 'MF':
            break
        print('Resposta inválida...')

    soma += dicionario['Idade']

    lista.append(dicionario.copy())

    escolha = str(input('Quer adicionar mais uma pessoa? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Resposta inválida...')
        escolha = str(input('Quer adicionar mais uma pessoa? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break

media = soma / len(lista)

print('\n' + '-='*30 + '\n')
print(f'Ao todo, foram cadastradas {len(lista)} pessoas.')
sleep(1)
print(f'A média de idade de todas as pessoas é de {media:.2f} anos.')
sleep(1)

print('As mulheres cadastradas foram:\n\t', end='')
for i in lista:
    if i['Sexo'] == 'F':
        print(f'\033[1m{i["Nome"]}\033[m |', end=' ')

print()
sleep(1)

print('As pessoas mais velhas que a média de idade são:\n\t', end='')
for i in lista:
    if i['Idade'] > media:
        print(f'\033[1m{i["Nome"]}\033[m com \033[1m{i["Idade"]}\033[m anos |', end=' ')
print()
