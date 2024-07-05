print('-='*20)
print('\033[1m{:^40}\033[m' .format('Venha descosbrir os termos de uma PA'))
print('-='*20)

qtde = int(input('\n\tAté quantos termos deseja ver? '))
prim = int(input('\tQual será o primeiro termo? '))
razao = int(input('\tQual será a razão? '))

num = prim
pa = prim + (qtde - 1) * razao

print('')

while num - razao != pa:
    print('{}'.format(num), end=' --> ')
    num += razao

print('FIM')
