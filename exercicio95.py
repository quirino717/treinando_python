lista = []
gols = []
dicionario = {}

while True:
    dicionario['Jogador'] = str(input('\nQual o nome do jogador: ')).capitalize().strip()
    partidas = int(input(f'{dicionario["Jogador"]} jogou em quantas partidas: '))
    gols.clear()
    for i in range(partidas):
        gols.append(int(input(f'\tQuantos gols marcou na {i + 1}° partida: ')))
    dicionario['Gols'] = gols[:]
    dicionario['Total'] = sum(gols)

    lista.append(dicionario.copy())

    escolha = str(input('Quer adicionar outro jogador? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Resposta inválida...')
        escolha = str(input('Quer adicionar outro jogador? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break

print('\n' + '\033[1m-=' * 30)
print('{:^60}'.format("Estatísticas"))
print('\033[1m-=\033[m' * 30 + '\n')

print('Cod ', end='')
for i in dicionario.keys():
    print(f'{i:<20}', end='')
print()
print(f'\033[4m-\033[m' * 60)

for c, v in enumerate(lista):
    print(f'{c:>3} ', end='')
    for dic in v.values():
        print(f'{str(dic):<20}', end='')
    print()
print(f'\033[4m-\033[m' * 60)

while True:
    jogador = int(input('\nDigite o Cod do jogador para ver os dados (999 encerra): '))

    if jogador == 999:
        print()
        print(f'{"FIM":-^60}')
        break

    if jogador >= len(lista):
        print('Não existe jogador com esse código de busca')
    else:
        print(f'O jogador \033[1;4m{lista[jogador]["Jogador"]}\033[m participou de \033[1;4m{len(lista[jogador]["Gols"])}\033[m jogos')
        for i, j in enumerate(lista[jogador]["Gols"]):
            print(f'\t->No {i + 1}° jogo fez \033[1;4m{j}\033[m gols')
        print(f'Totalizando \033[1;4m{lista[jogador]["Total"]}\033[m gols.')
