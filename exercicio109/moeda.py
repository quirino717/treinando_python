def aumentar(x=0, taxa=0, formatacao=False):
    resultado = x + (x * taxa/100)
    return resultado if formatacao is False else moeda(resultado)


def diminuir(x=0, taxa=0, formatacao=False):
    resultado = x - (x * taxa/100)
    return resultado if formatacao is False else moeda(resultado)


def dobro(x=0, formatacao=False):
    resultado = x * 2
    return resultado if formatacao is False else moeda(resultado)


def metade(x=0, formatacao=False):
    resultado = x / 2
    return resultado if formatacao is False else moeda(resultado)


def moeda(x=0, moeda='R$'):
    return f'\033[1;32m{moeda}{x:.2f}\033[m'.replace('.', ',')
