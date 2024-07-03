preço = float(input('Valor total do produto: R$'))
desconto = float(input('Porcentagem do desconto: '))

pf = preço - preço*(desconto/100)

print('\nValor final: R${:.2f}'.format(pf))