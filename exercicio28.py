import random

num = random.randint(1, 10)

adivinha = int(input('\n\tEstou pensando em um número entre 1 a 10\n'
                     '\tTente adivinhar qual é: '))

if adivinha == num:
    print('\nParabéns, \033[1;34mvocê acertou!!\033[m\nO número que pensei era o \033[4m{}\033[m mesmo' .format(num))
else:
    print('\nQue pena, \033[1;31mvocê errou!!\033[m\nEstava pensando no número \033[4m{}\033[m' .format(num))
