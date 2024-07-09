print('\033[1m-='*20)
print('{:^40}' .format("Mercadinho Big Boom"))
print('\033[1m-=\033[m'*20 + '\n')

itens = ('Lápis', 1.75, 'Borracha', 1.5, 'Caderno', 15.90, 'Estojo', 20, 'Trasnferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.30, 'Canetas', 22.30, 'Livro', 34.90)

for i in range(0, len(itens)):
    if i % 2 == 0:
        print(f'{itens[i]:.<30} ', end='R$ ')
    if i % 2 != 0:
        print(f'{itens[i]:.2f}\n', end='')
