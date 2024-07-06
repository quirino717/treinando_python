

while True:
    num = int(input('\nDigite o número que você deseja saber a tabuada: '))

    print('\nA tabuada do número {} é:'.format(num))
    print('-' * 20)

    for i in range(1, 11):
        print('{} x {} = \033[1m{}\033[m'.format(num, i, num * i))

    print('-' * 20)

    if num < 0:
        break

print('Volte sempre!')
