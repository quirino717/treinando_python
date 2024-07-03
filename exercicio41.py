from datetime import date

print('\033[35m-='*20)
print('{:^40}'.format('Confederação Nacional de Natação'))
print('\033[35m-=\033[m'*20)

ano = int(input('\n\tInforme o ano do seu nascimento: '))

idade = date.today().year - ano

print('\n\tEntão você tem {} anos\n\tO que faz você da categoria: ' .format(idade), end='')

if idade <= 9:
    print('\033[1;34mMIRIM\033[m')
elif idade <= 14:
    print('\033[1;34mINFANTIL\033[m')
elif idade <= 19:
    print('\033[1;34mJÚNIOR\033[m')
elif idade <= 25:
    print('\033[1;34mSÊNIOR\033[m')
else:
    print('\033[1;34mMASTER\033[m')