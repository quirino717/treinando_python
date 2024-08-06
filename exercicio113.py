def inteiro(txt):
    while True:
        try:
            n = int(input(txt))
        except (TypeError, ValueError):
            print('\033[1;31mERRO!!\033[m \033[31mPor favor digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\nUsuário interrompeu o programa')
            return 0
        else:
            return n


def real(txt):
    while True:
        try:
            n = float(input(txt))
        except (TypeError, ValueError):
            print('\033[1;31mERRO!!\033[m \033[31mPor favor digite um número real válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\nUsuário interrompeu o programa')
            return 0
        else:
            return n


inte = inteiro('Digite um número inteiro: ')
r = real('Digite um número real: ')
print(f'\nO valor inteiro digitado foi {inte}\nO valor real digitado foi {r}')
