from time import sleep


def cont(ini, fim, passo):
    passo = abs(passo)
    if passo == 0:
        passo = 1

    print(f'\nContando de {ini} até {fim} pulando de {passo} em {passo}')
    sleep(0.25)

    print('Início -> ', end='')
    if ini < fim:
        while ini <= fim:
            print(f'\033[1m{ini}', end=' ')
            ini += passo
            sleep(0.5)
        print('\033[m<- FIM\n')
    elif ini > fim:
        while ini >= fim:
            print(f'\033[1m{ini}', end=' ')
            ini -= passo
            sleep(0.5)
        print('\033[m<- FIM\n')


cont(1, 10, 1)
cont(10, 0, 2)

inicio = int(input('\nInforme um valor para começar: '))
final = int(input('Informe um valor para terminar: '))
pulo = int(input('Informe o passo da contagem: '))
cont(inicio, final, pulo)
