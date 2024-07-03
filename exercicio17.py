from math import sqrt, hypot

co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))

#hip = sqrt(co**2 + ca**2)
hip = hypot(co, ca)

print('\nA hipotenusa desse triangulo será de {:.2f}' .format(hip))