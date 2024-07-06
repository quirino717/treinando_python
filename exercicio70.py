from time import sleep

print('\033[1;35m-='*20)
print('{:^40}' .format('Mercadinho Big Boom'))
print('\033[1;35m-=\033[m'*20)

soma = qtde = baratopreco = produtos = 0
barato = ''



while True:
    produto = str(input('\n\tQual o produto: ')).strip().capitalize()
    preco = float(input('\tQual o preço: R$'))

    soma += preco
    produtos += 1

    if produtos == 1:
        barato = produto
        baratopreco = preco
    else:
        if preco < baratopreco:
            barato = produto
            baratopreco = preco

    if preco > 1000:
        qtde += 1

    continuar = str(input('\tDeseja passar mais um? [S/N] ')).strip().upper()[0]

    while continuar not in 'SN':
        print('\n\tOpção inválida')
        continuar = str(input('\tDeseja passar mais um? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        print(f'\n\tAnalisando produtos todos os {produtos} produtos...')
        break

sleep(1)

print(f'\n\tO total da sua compra é R${soma:.2f}')
print(f'\t{qtde} produtos custam mais de R$1000.00')
print(f'\tO produto mais barato custa R${baratopreco:.2f} e foi {barato}')


