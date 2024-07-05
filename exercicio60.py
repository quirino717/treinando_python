from math import factorial

num = int(input('Digite um número para descobrir seu fatorial: '))
resultado = factorial(num)
print('\n{}! = '.format(num, num), end='')

while num != 0:
    print('{} ' .format(num), end='')
    print('x '.format(resultado) if num > 1 else '= ', end='')
    num -= 1

print('{}' .format(resultado))

