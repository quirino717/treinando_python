print('-='*20)
print('\033[1m{:^40}\033[m' .format('Somador'))
print('-='*20)
print()

cont = soma = 0

while True:
    num = float(input('Digite um valor (999 para parar): '))

    if num == 999:
        break

    cont += 1
    soma += num

print(f'\nVocê digitou \033[4m{cont}\033[m números\nE a soma de todos é: \033[1m{soma}')
