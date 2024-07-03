print('\033[34m-='*25)
print('\tBem-vindo ao analisador de triângulos')
print('\033[34m-=\033[m'*25)

num = []

print()

for i in range (1, 4):
    num.append(float(input('\tDigite o valor da {}° reta: ' .format(i))))

tipo = str

if num[0] == num[1] == num[2]:
    tipo = 'equilátero'
elif num[0] != num[1] != num[2]:
    tipo = 'escaleno'
else:
    tipo = 'isóceles'

if num[0] + num[1] > num[2] and num[2] + num[1] > num[0] and num[0] + num[2] > num[1]:
    print('\nCom esses valores \033[1;32mÉ POSSÍVEL\033[m construir um triângulo \033[1;36m{}\033[m' .format(tipo))
else:
    print('\nCom esses valores \033[1;31mNÃO É POSSÍVEL\033[m construir um triângulo')