print('\033[1;35m-='*20)
print('{:^40}' .format('Inversor de frases'))
print('\033[1;35m-=\033[m'*20)

frase = str(input('\n\tEscreva uma frase: ')).upper().strip()
palavras = frase.split()
juntar = ''.join(palavras)
contrario = juntar[::-1]

'''for i in range(len(juntar) - 1, -1, -1):
    contrario += juntar[i]'''

print('\n\t\033[4m{}\033[m\n\tescrito ao contrário fica\n\t\033[4m{}\033[m' .format(juntar, contrario))

if contrario == juntar:
    print('\n\tA frase digitada \033[1mé um palíndromo\033[m')
else:
    print('\n\tA frase digitada \033[1mnão é um palíndromo\033[m')