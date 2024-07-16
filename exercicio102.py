from math import factorial


def fatorial(num, mostra=False):
    """
    -> Calcula o fatorial do número de entrada
    :param num: número a ter seu fatorial calculado
    :param mostra: mostra todo o cálculo ou não
    :return: o resultado
    """

    print('\n' + '-'*40)
    fat = factorial(num)
    if mostra:
        print(f'{num}! = ', end='')
        while num > 0:
            print(f'{num} x' if num != 1 else f'{num}', end=' ')
            num -= 1
        print(f'= {fat}')
    else:
        print(f'{num}! = {fat}')
    return fat


x = int(input('\nDigite o número que quer saber o fatorial: '))
show = str(input('Quer ver todo o cálculo (S/N)? ')).upper().strip()[0]

if show == 'S':
    show = fatorial(x, True)
else:
    show = fatorial(x, False)

#help(fatorial)
