qtde = int(input('\nDeseja analisar o peso de quantas pessoas? '))
print('')

maior = menor = 0

for i in range(1, qtde + 1):
    peso = float(input('Informe o peso da {}° pessoa: '.format(i)))
    if i == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('\nDentre essas pessoas, a mais pesada tem {}Kg\ne a mais leve {}Kg' .format(maior, menor))