def area(b, h):
    print(f'\nA área de um terreno de {b:.2f}x{h:.2f} é de {b*h:.2f}m²')


print(f'{"Controle de terrenos":^40}')
print('-' * 40)

l = float(input('\nQual a largura do terreno em m: '))
c = float(input('Qual a altura do terreno em m: '))

area(l, c)
