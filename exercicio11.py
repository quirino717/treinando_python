alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))

area = alt * larg
tinta = area / 2

print('\nPara uma parede de {}x{}, com área de {:.2f}m²,\né necessário {:.2f}l de tinta' .format(alt, larg, area, tinta))