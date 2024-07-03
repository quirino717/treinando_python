dr = int(input('Digite 1 para converter reais em dólares\nDigite 2 para converter dólares em reais\nO que deseja fazer: '))

if dr == 1:
    reais = float(input('\nDigite quantos reais você quer converter: R$'))

    print('\nR${} equivalem a ${:.2f}' .format(reais,(reais/5.59)))

if dr == 2:
    dolares = float(input('\nDigite quantos dólares você quer converter: $'))

    print('\n${} equivalem a R${:.2f}' .format(dolares,(dolares*5.59)))


