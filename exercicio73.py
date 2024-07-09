from time import sleep

print('\033[1;32m-='*20)
print('{:^40}' .format("Brasileirão"))
print('\033[1;32m-=\033[m'*20)

times = ('Flamengo', 'Botafogo', 'Palmeiras', 'São Paulo', 'Bahia', 'Athletico-Pr', 'Cruzeiro', 'Fortaleza', 'Bragantino', 'Internacional',
         'Juventude', 'Atlético-Mg', 'Vasco', 'Criciúma', 'Vitória', 'Cuiabá', 'Corinthians', 'Grêmio', 'Atlético-Go', 'Fluminense')

while True:
    print('\n\tO que deseja fazer?'
          '\n\tDigite \033[4m1\033[m para ver os 5 primeiros'
          '\n\tDigite \033[4m2\033[m para ver os 4 últimos'
          '\n\tDigite \033[4m3\033[m para ver os times em ordem alfabética'
          '\n\tDigite \033[4m4\033[m para ver a posição de um time'
          '\n\tDigite \033[4m5\033[m para ver um time em uma posição'
          '\n\tDigite \033[4m6\033[m para sair')

    escolha = int(input('\n\tQual a sua escolha? '))

    if escolha == 1:
        print('\n\tEsses são os 5 primeiros colocados:')
        for i in range(5):
            print(f'\t{i + 1}° - {times[i]}')
        sleep(1)

    elif escolha == 2:
        print('\n\tEsses são os 4 últimos colocados:')
        i = 17
        while i <= 20:
            print(f'\t{i}° - {times[i - 1]}')
            i += 1
        sleep(1)

    elif escolha == 3:
        print(f'\n\tEsses os 20 primeiros colocados:'
              f'\n\t{sorted(times)}')
        sleep(1)

    elif escolha == 4:
        nome = str(input('\n\tQual o time que deseja procurar? ')).strip().title()

        if nome in times:
            print(f'\n\tO time {nome} está na \033[1m{times.index(nome) + 1}°\033[m posição')
            sleep(1)
        else:
            print('\n\tEsse time não está na lista')
            sleep(1)

    elif escolha == 5:
        posicao = int(input('\n\tQual posição deseja checar? '))
        print(f'\n\tO time \033[1m{times[posicao - 1]}\033[m está na {posicao}° posição')
        sleep(1)

    elif escolha == 6:
        break