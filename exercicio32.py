from time import sleep
from datetime import date

ano = int(input('\n\tDigite um ano e diriei se foi bissexto ou não\n\tPara analisar o ano atual digite 0: '))

print('\nAnalisando', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\n\t{} \033[1;32mé\033[m um ano bissexto'.format(ano))
else:
    print('\n\t{} \033[1;31mnão\033[m é um ano bissexto'.format(ano))

