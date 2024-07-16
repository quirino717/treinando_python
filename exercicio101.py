from datetime import date


def voto(a):
    idade = date.today().year - a
    if idade < 16:
        print(f'Com {idade} anos, \033[1;31mvocê não vota\033[m')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos, seu voto é \033[1;33mopcional\033[m')
    else:
        print(f'Com {idade} anos, seu voto é \033[1;32mobrigatório\033[m')


ano = int(input('Em que ano você nasceu? '))
voto(ano)
