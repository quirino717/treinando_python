num = []

print()

for i in range (1, 4):
    num.append(float(input('\tDigite o valor da {}° reta: ' .format(i))))

if num[0] + num[1] > num[2] and num[2] + num[1] > num[0] and num[0] + num[2] > num[1]:
    print('\nCom esses valores \033[1;32mÉ POSSÍVEL\033[m construir um triângulo')
else:
    print('\nCom esses valores \033[1;31mNÃO É POSSÍVEL\033[m construir um triângulo')