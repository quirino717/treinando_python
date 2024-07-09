tupla = ('alfabeto', 'cachorro', 'livro', 'computador', 'bicicleta', 'celular', 'mesa', 'cadeira', 'janela', 'telefone')

for i in tupla:
    print(f'\nA palavra \033[1;4m{i.capitalize()}\033[m tem as seguintes vogais: ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(f'\033[1m{letra.upper()}\033[m', end=' ')
