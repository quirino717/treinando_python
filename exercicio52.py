print('-='*20)
print('\033[1m{:^40}\033[m' .format('Venha descosbrir se o número é primo'))
print('-='*20)

num = int(input('\n\tDigite um número e direi se é primo ou não: '))
print('')
primo = 0

if num > 1:
    for i in range(1, num + 1):
        if num % i == 0:
            print('\t\033[1;32m', end='')
            primo += 1
        else:
            print('\t\033[1;31m', end='')
        print('{}'.format(i), end=' ')

    print('\033[m\n\n\tO número {} foi divido {} vezes'.format(num, primo))
    if primo == 2:
        print('\tO que faz dele um \033[1mnúmero primo\033[m')
    else:
        print('\tO que faz dele um \033[1mnúmero não primo\033[m')
else:
    print('\tEsse número \033[1mnão é primo\033[m')