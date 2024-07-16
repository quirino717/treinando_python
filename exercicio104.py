def inteiro(frase):
    x = 0
    while True:
        n = str(input(frase))
        if n.isnumeric():
            x = int(n)
            break
        else:
            print('\033[31mValor de entrada inválido!!\033[m')
    return x


numero = inteiro('Digite um número: ')
print(f'Você digitou o número: {numero}')
