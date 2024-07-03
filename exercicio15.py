dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Por quantos km você andou com o carro? '))

valor = (dias * 60) + (km * 0.15)

print('\nO valor a pagar pelo aluguel do carro é de R${:.2f}' .format(valor))