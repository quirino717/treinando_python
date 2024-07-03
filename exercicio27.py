from time import sleep

nome = str(input('Informe seu nome completo: ')).strip().capitalize()

print('\nAnalisando o seu nome', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.\n')
sleep(0.5)

print('Seu primeiro nome é: {}' .format(nome.split()[0]))
print('Seu último nome é: {}' .format(nome.split()[len(nome.split()) - 1].capitalize()))
