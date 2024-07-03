print('\033[34m-='*25)
print('\tBem-vindo ao comparador de números')
print('\033[34m-=\033[m'*25)

num1 = float(input('\n\tDigite o 1° número para ser comparado: '))
num2 = float(input('\tDigite o 2° número para ser comparado: '))

if num1 > num2:
    print('\n\tO \033[1;35mprimeiro\033[m número é o maior!')
elif num2 > num1:
    print('\n\tO \033[1;35msegundo\033[m número é o maior!')
else:
    print('\n\tOs dois números \033[1;35msão iguais!\033[m')