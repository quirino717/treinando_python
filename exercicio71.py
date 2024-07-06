from time import sleep

print('\033[1;32m-='*20)
print('{:^40}' .format("Quirino's Bank"))
print('\033[1;32m-=\033[m'*20)

valor = int(input('\n\tO quanto gostaria de sacar hoje: R$'))

print('\n\tSacando o valor em:\n')
sleep(1)

total = valor
cedula = 100
totced = 0

while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'\t\033[1m{totced}\033[m cédulas de \033[1;32mR${cedula}\033[m')

        if cedula == 100:
            cedula = 50
            totced = 0
        elif cedula == 50:
            cedula = 20
            totced = 0
        elif cedula == 20:
            cedula = 10
            totced = 0
        elif cedula == 10:
            cedula = 5
            totced = 0
        elif cedula == 5:
            cedula = 2
            totced = 0

        if total == 0:
            break

print('\n\tObrigado pela preferência\n\tVolte sempre')
