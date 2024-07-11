matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma = soma3 = maior = 0

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Digite um valor para a posição [{i+1}][{j+1}]: '))

        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]

        soma3 += matriz[i][2]

        if matriz[1][j] == 0:
            maior = matriz[1][j]
        else:
            if matriz[1][j] > maior:
                maior = matriz[1][j]

print()

for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()

print(f'\nA soma de todos os valores pares dessa matriz é: {soma}')
print(f'A soma de todos os da terceira coluna é: {soma3}')
print(f'O maior valor na segunda linha é: {maior}')