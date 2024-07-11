dicionario = {}
gols = []
total = 0

dicionario['Nome'] = str(input('Qual o nome do jogador: ')).capitalize().strip()
partidas = int(input(f'Quantas partidas {dicionario["Nome"]} jogou: '))

for i in range(partidas):
    gols.append(int(input(f'Quantos gols na {i + 1}° partida: ')))
    dicionario['Gols'] = gols[:]
    dicionario['Total'] = sum(gols)

print()
print('-'*40)
print(dicionario)
print('-'*40)

for c, v in dicionario.items():
    print(f'{c} = {v}')
print('-'*40)

print(f'O jogador {dicionario["Nome"]} participou de {partidas} jogos')
for i in range(partidas):
    print(f'\t->No {i + 1}° jogo fez {gols[i]} gols')
print(f'Totalizando {dicionario["Total"]} gols.')
