'''lista = []

for i in range(1,10):
    lista.append(int(input(f'Digite o {i}° número: ')))

print(f'\n[{lista[0]}] [{lista[1]}] [{lista[2]}]'
      f'\n[{lista[3]}] [{lista[4]}] [{lista[5]}]'
      f'\n[{lista[6]}] [{lista[7]}] [{lista[8]}]')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Digite um valor para a posição [{i+1}][{j+1}]: '))

print()

for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
