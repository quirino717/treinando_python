from random import randint
from time import sleep

print('\033[1m-='*20)
print('{:^40}' .format("Loteria"))
print('\033[1m-=\033[m'*20 + '\n')

jogos = []
nums = []
cont = 0
qtde = int(input('\tQuantos jogos quer gerar? '))

print('\n\tSorteando números...')
sleep(0.5)

while cont < qtde:
    contador = 0
    while True:
        num = randint(1, 60)

        if num not in nums:
            nums.append(num)
            contador += 1

        if contador == 6:
            break

    nums.sort()
    jogos.append(nums[:])
    nums.clear()
    cont += 1

print()
for i in range(qtde):
    print(f'\tJogo {i+1}: {jogos[i]}')
    sleep(1)
