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
    return f'\t\t\033[1;32m{moeda:}{x:.2f}\033[m'.replace('.', ',')


def resumo(x=0, aumento=0, diminui=0):
    print('\n' + '\033[1m-' * 33)
    print('RESUMO DO VALOR'.center(33))
    print('\033[1m-\033[m' * 33)
    print(f'Preço analisado: {moeda(x):}')
    print(f'Dobro do preço: {dobro(x, True)}')
    print(f'Metade do preço: {metade(x, True)}')
    print(f'{aumento}% de aumento: {aumentar(x, aumento, True)}')
    print(f'{diminui}% de redução: {diminuir(x, diminui, True)}')
    print('\033[1m-' * 33)
