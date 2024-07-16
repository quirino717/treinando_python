from random import randint
from time import sleep


def aleatorio(lista):
    print('Sorteando valores: \033[1m', end='')
    for i in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[i], end=' ')
        sleep(0.5)
    print('\033[m- Valores sorteados')


def pares(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'A soma de todos os números pares sorteados é: \033[1m{soma}\033[m')


nums = []
aleatorio(nums)
pares(nums)
