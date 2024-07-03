print('-='*20)
print('\033[1m{:^40}\033[m' .format('Venha descosbrir os termos de uma PA'))
print('-='*20)

qtde = int(input('\n\tAté quantos termos deseja ver? '))
prim = int(input('\tQual será o primeiro termo? '))
razao = int(input('\tQual será a razão? '))

pa = prim + (qtde - 1) * razao

for i in range(prim, pa+1, razao):
    print('{}' .format(i), end=' --> ')

print('FIM')
