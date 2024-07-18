from exercicio109 import moeda

dinheiro = float(input('Digite um preço: R$'))
print(f'\nO dobro de {moeda.moeda(dinheiro)} é {moeda.dobro(dinheiro, True)}')
print(f'A metade de {moeda.moeda(dinheiro)} é {moeda.metade(dinheiro, True)}')
print(f'\nAo aumentarmos em 10%: {moeda.aumentar(dinheiro, 10, True)}')
print(f'Ao diminuitmos em 10%: {moeda.diminuir(dinheiro, 10, True)}')
