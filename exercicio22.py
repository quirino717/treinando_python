from time import sleep

nome = str(input('Informe seu nome completo: ')).strip()

print('\nAnalisando o seu nome', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.\n')
sleep(0.5)

#dividido = nome.split()

print('Imprimindo com letras maiusculas: {}' .format(nome.upper()))
print('Imprimindo com letras maiusculas: {}' .format(nome.lower()))
print('Seu nome tem {} letras' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
#print('Seu primeiro nome tem {} letras' .format(len(dividido[0])))
