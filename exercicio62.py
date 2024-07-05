print('-='*20)
print('\033[1m{:^40}\033[m' .format('Venha descosbrir os termos de uma PA'))
print('-='*20)

qtde = int(input('\n\tAté quantos termos deseja ver? '))
prim = int(input('\tQual será o primeiro termo? '))
razao = int(input('\tQual será a razão? '))

num = prim
total = 0
cont = 1

print('')

while qtde != 0:
    total += qtde

    while cont <= total:
        print('{}'.format(num), end=' --> ')
        num += razao
        cont += 1

    print('PAUSA')
    qtde = int(input('Quantos termos a mais deseja ver: '))

print('\nEncerrando')
