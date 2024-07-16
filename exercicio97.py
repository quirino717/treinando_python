def titulo(txt):
    cont = len(txt) + 4
    print('\033[1;34m-' * cont)
    print(f'  {txt.title()}')
    print('\033[1;34m-\033[m' * cont)


frase = str(input('Digite uma frase: ')).strip()

titulo(frase)
