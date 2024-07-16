from time import sleep
from random import randint

def maior(* lista):
    print('\nAnalisando os valores de entrada...')
    cont = m = 0
    while cont < len(lista):
        print(lista[cont], end=' ')
        if cont == 0:
            m = lista[cont]
        else:
            if lista[cont] > m:
                m = lista[cont]
        cont += 1
        sleep(0.5)
    print(f'\nForam informados \033[1m{cont}\033[m valores')
    print(f'O maior valor foi: \033[1m{m}\033[m')


maior(2, 9, 4, 5, 7, 1)
maior(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
maior()


