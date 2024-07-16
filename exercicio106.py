from time import sleep


def titulo_azul(txt):
    cont = len(txt) + 4
    print('\033[1;34m-' * cont)
    print(f'  {txt}')
    print('\033[1;34m-\033[m' * cont + '\n')


def titulo_verde(txt):
    cont = len(txt) + 4
    print('\033[1;32m-' * cont)
    print(f'  {txt}')
    print('\033[1;32m-\033[m' * cont + '\n')


def titulo_vermelho(txt):
    cont = len(txt) + 4
    print('\n' + '\033[1;31m-' * 60)
    print(f'{txt:^60}')
    print('\033[1;31m-\033[m' * 60 + '\n')


def ajuda(txt):
    while True:
        titulo_azul('Sistema de ajuda - PyHelp')
        sleep(0.5)
        comando = str(input(txt)).strip().upper()

        if comando == 'FIM':
            titulo_vermelho('Até mais!!')
            break

        print()
        titulo_verde(f'Abrindo manual do comando: {comando.lower()}')
        sleep(0.5)

        print(f'\033[1;33;40m')
        help(comando.lower())
        print(f'\033[m')
        sleep(1)

    return comando


duvida = ajuda('Digite uma função ou biblioteca: ')
