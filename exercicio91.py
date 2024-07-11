from random import randint
from time import sleep
from operator import itemgetter

dicionario = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6), 'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6)}
colocacao = []

print('Os jogadores tiraram:')
for k, v in dicionario.items():
    print(f'O {k} tirou {v}')
    sleep(1)

colocacao = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
print('\nA colocação ficou da seguinte forma: ')

for i, j in enumerate(colocacao):
    print(f'{i + 1}° lugar - {j[0]} que tirou {j[1]}')
    sleep(1)

