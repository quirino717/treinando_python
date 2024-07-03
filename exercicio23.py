from time import sleep
num = int(input('Digite um número: '))

print('\nAnalisando o número {}' .format(num), end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.\n')
sleep(0.5)

print('Unidade: {}' .format(num // 1 % 10))
print('Dezena: {}' .format(num // 10 % 10))
print('Centena: {}' .format(num // 100 % 10))
print('Milhar: {}' .format(num // 1000 % 10))
