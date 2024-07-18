def leiadinheiro(msg):
    while True:
        dinheiro = str(input(msg)).strip()

        if dinheiro.isnumeric():
            break
        else:
            if dinheiro == '' or dinheiro.isalpha():
                print(f'\033[1;31mERRO!!!\033[m \033[31m"\033[1;4m{dinheiro}\033[m\033[31m" é um preço inválido\033[m\n')

            if ',' in dinheiro:
                dinheiro = dinheiro.replace(',', '.')
                break

    return float(dinheiro)
