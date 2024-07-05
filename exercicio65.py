cont = soma = maior = menor = 0
escolha = 's'

while escolha in 'Ss':
    num = int(input('\nDigite um valor: '))
    soma += num
    cont += 1

    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    escolha = str(input('Deseja continuar (s/n)? ')).strip()[0]

    if escolha not in 'NnSs':
        print('\nOpção inválida')
        escolha = str(input('Deseja continuar (s/n)? ')).strip()[0]

print('\nVocê digitou {} números e a média entre eles é {:.2f}' .format(cont, (soma / cont)))
print('O maior número entre eles é {} e o menor é {}' .format(maior, menor))