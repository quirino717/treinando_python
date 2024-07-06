from random import randint
from time import sleep

print('\033[1;35m-='*20)
print('{:^40}' .format('Par ou Ímpar'))
print('\033[1;35m-=\033[m'*20)

while True:
    escolha = str(input('\n\tPar ou Ímpar: ')).strip().upper()[0]
    num = int(input('\tQual número você vai jogar: '))
    computador = randint(0, 10)

    soma = num + computador

    print()
    print(' ' * 10 + '\033[1m{}'.format('Par '), end='')
    sleep(0.5)
    print('ou ', end='')
    sleep(0.5)
    print('Ímpar\033[m')
    sleep(0.5)

    print(f'\n\tEu escolhi {computador} e você {num}\n\tA soma é {computador + num}, então...')
    sleep(1)

    if escolha == 'P' and soma % 2 == 0:
        print('\n\t\033[1mDeu PAR!\033[m')
        print('\n\t\033[1;32mVocê me venceu!!\033[m\n\tPARABÉNS :D')
    elif escolha == 'P' and soma % 2 != 0:
        print('\n\t\033[1mDeu ÍMPAR!\033[m')
        print('\n\t\033[1;31mEu te venci!!\033[m\n\tQue pena :(')
    elif escolha in 'IÍ' and soma % 2 != 0:
        print('\n\t\033[1mDeu ÍMPAR!\033[m')
        print('\n\t\033[1;32mVocê me venceu!!\033[m\n\tPARABÉNS :D')
    elif escolha in 'IÍ' and soma % 2 == 0:
        print('\n\t\033[1mDeu PAR!\033[m')
        print('\n\t\033[1;31mEu te venci!!\033[m\n\tQue pena :(')

    sleep(1)

    dnv = str(input('\n\tGostaria de jogar de novo (S/N)? ')).strip().upper()[0]

    if dnv == 'N':
        break

sleep(1)
print('\n\tEspero jogar com você de novo :)')
