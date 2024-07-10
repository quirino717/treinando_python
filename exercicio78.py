lista = []
menor = maior = 0

for i in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))

    if i == 0:
        menor = maior = lista[i]
    else:
        if lista[i] < menor:
            menor = lista[i]
        if lista[i] > maior:
            maior = lista[i]

print(f'\nVocê digitou os seguintes valores: {lista}')
print(f'O maior valor digitado foi {maior} e esta na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}')

print(f'O menor valor digitado foi {menor} e esta na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}')
        