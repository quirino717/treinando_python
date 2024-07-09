from random import randint

tupla = (randint(0,99), randint(0,99), randint(0,99), randint(0,99), randint(0,99))

print('Os valores sorteados foram: ', end='')
for i in tupla:
    print(i, end=' ')

print(f'\n\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
