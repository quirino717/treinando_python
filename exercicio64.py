print('-='*20)
print('\033[1m{:^40}\033[m' .format('Somador'))
print('-='*20)

num = float(input('\nDigite um valor (999 para parar): '))
cont = soma = 0

while num != 999:
    cont += 1
    soma += num
    num = float(input('Digite um valor (999 para parar): '))

print('\nVocê digitou \033[4m{}\033[m números\nE a soma de todos é: \033[1m{}' .format(cont, soma))