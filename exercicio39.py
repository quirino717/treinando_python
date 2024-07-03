from datetime import date

print('\033[32m-='*25)
print('{:^50}'.format('Exército'))
print('\033[32m-=\033[m'*25)

ano = int(input('\n\tInforme o ano do seu nascimento: '))

idade = date.today().year - ano

print('\n\tEntão você tem {} anos'.format(idade))

if idade < 18:
    print('\tO que significa que faltam {} para você se alistar'
          '\n\tVocê deve se alistar em {}' .format((18 - idade), (date.today().year + (18 - idade))))
elif idade == 18:
    print('\tPara o seu bem, é bom que já esteja alistado!!!')
else:
    print('\tO que significa que seu alistamento foi a {} anos atrás em {}'
          '\n\tÉ bom que você tenha se alistado!!!' .format((idade - 18), (date.today().year - (idade - 18))))