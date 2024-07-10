lista = []

for i in range(0,5):
    num = int(input('Digite um valor: '))

    if lista == [] or num > lista[-1]:
        lista.append(num)
        print('Valor adicionado no final da lista')
    else:
        pos = 0

        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num)
                print(f'Valor adicionado na posição {pos}')
                break

            pos += 1

print(f'\nA lista em ordem crescente fica: {lista}')
