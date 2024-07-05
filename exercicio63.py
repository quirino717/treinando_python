print('-='*20)
print('\033[1m{:^40}\033[m' .format('Sequência de Fibonacci'))
print('-='*20)

qtde = int(input('\n\tQuantos termos deseja ver? '))
prim = int(input('\tQual será o primeiro termo? '))
segu = int(input('\tQual será o segundo termo? '))

cont = 3

print('\n{} --> {} --> ' .format(prim, segu), end='')

while cont <= qtde:
    cont += 1
    prox = prim + segu
    prim = segu
    segu = prox

    print('{} --> '.format(prox), end='')

print('FIM')
