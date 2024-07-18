from exercicio107 import moeda

dinheiro = float(input('Digite um preço: R$'))
print(f'\nO dobro de R${dinheiro:.2f} é R${moeda.dobro(dinheiro):.2f}')
print(f'A metade de R${dinheiro:.2f} é R${moeda.metade(dinheiro):.2f}')
print(f'\nAo aumentarmos em 10%: {moeda.aumentar(dinheiro, 10):.2f}')
print(f'Ao diminuitmos em 10%: {moeda.diminuir(dinheiro, 10):.2f}')
