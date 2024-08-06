from time import sleep


def titulo(txt):
    #cont = len(txt) + 4
    print('\n' + '\033[1m-' * 60)
    print(f'{txt.center(60)}')
    print('\033[1m-\033[m' * 60 + '\n')


def linha():
    print('\n' + '\033[1m-\033[m' * 60)


def inteiro(frase):
    x = 0
    while True:
        n = str(input(frase))
        if n.isnumeric():
            x = int(n)
            break
        else:
            print('\033[31mValor de entrada inválido!!\033[m')
    return x


def sair():
    linha()
    print('\nEncerrando o programa', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('Até logo')
    linha()


def menu(lista):
    titulo('Sistema de cadastros')
    cont = 1
    for item in lista:
        print(f'\033[1;4;33m{cont}\033[m - \033[1;4m{item}\033[m')
        cont += 1
    linha()
    opc = inteiro('\nO que deseja fazer? ')
    return opc

