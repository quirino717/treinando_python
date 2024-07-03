print('\033[34m-='*25)
print('\tBem-vindo ao conversor de números')
print('\033[34m-=\033[m'*25)

num = int(input('\n\tDigite o número que gostaria de converter: '))

print('\n\tAgora escolha a base para a conversão'
      '\n\n\tDigite \033[1;4m1\033[m para converter em binário'
      '\n\tDigite \033[1;4m2\033[m para converter em octal'
      '\n\tDigite \033[1;4m3\033[m para converter em hexadecimal')
escolha = int(input('\tO que deseja fazer: '))

if escolha == 1:
    print('\n\tO número {} em binário fica da seguinte forma: \033[1;32m{}\033[m' .format(num, bin(num)[2:]))
elif escolha == 2:
    print('\n\tO número {} em octal fica da seguinte forma: \033[1;32m{}\033[m'.format(num, oct(num)[2:]))
else:
    print('\n\tO número {} em hexadecimal fica da seguinte forma: \033[1;32m{}\033[m'.format(num, hex(num)[2:]))
