from time import sleep
frase = str(input('Digite uma frase qualquer: ')).strip().upper()

print('\nAnalisando a frase', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.\n')
sleep(0.5)

print('A letra "A" aparece {} vezes na frase' .format(frase.count('A')))
print('Aparece pela primeira vez na posição {}' .format(frase.find('A') + 1))
print('Aparece pela última vez na posição {}' .format(frase.rfind('A') + 1))
