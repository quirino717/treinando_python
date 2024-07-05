from random import randint
from time import sleep
import os

print('\033[1;35m-='*20)
print('{:^40}' .format('Adivinhe o número'))
print('\033[1;35m-=\033[m'*20)

sleep(0.5)

print('\n\tEstou pensando em um número entre 1 e 10\n\tSerá que você consegue adivinhar?')

num = randint(1, 10)
tentativas = 0

sleep(0.5)

adivinha = int(input('\n\tQual seu palpite? '))

while adivinha != num:
    tentativas += 1

    if adivinha < num:
        adivinha = int(input('\n\tVocê \033[1;31merrou!!\033[m\n\t{} é menor do que a resposta\n\tTente outro palpite: ' .format(adivinha)))
    if adivinha > num:
        adivinha = int(input(
            '\n\tVocê \033[1;31merrou!!\033[m\n\t{} é maior do que a resposta\n\tTente outro palpite: '.format(
                adivinha)))

print('\n\tPARABÉNS!!\n\tVocê \033[1;32macertou\033[m com {} tentativas!!\n\tO número era {} mesmo' .format(tentativas, num))
