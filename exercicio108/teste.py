from exercicio108 import moeda

dinheiro = float(input('Digite um preço: R$'))
print(f'\nO dobro de {moeda.moeda(dinheiro)} é {moeda.moeda(moeda.dobro(dinheiro))}')
print(f'A metade de {moeda.moeda(dinheiro)} é {moeda.moeda(moeda.metade(dinheiro))}')
print(f'\nAo aumentarmos em 10%: {moeda.moeda(moeda.aumentar(dinheiro))}')
print(f'Ao diminuitmos em 10%: {moeda.moeda(moeda.diminuir(dinheiro))}')
