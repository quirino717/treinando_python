def aumentar(x=0, taxa=0):
    return x + (x * taxa/100)


def diminuir(x=0, taxa=0):
    return x - (x * taxa/100)


def dobro(x=0):
    return x * 2


def metade(x=0):
    return x / 2


def moeda(x=0, moeda='R$'):
    return f'\033[1;32m{moeda}{x:.2f}\033[m'.replace('.', ',')
