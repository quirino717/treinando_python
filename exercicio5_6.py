from math import sqrt

num = int(input('Digite um número: '))
ant = num - 1
suc = num + 1
dobro = num * 2
triplo = num * 3
raiz = sqrt(num)
print('\nO número {} tem como antecessor {} e sucessor {}.\nSeu dobro é {} e seu triplo é {}.\nSua raiz quadrada é {:.2f}' .format(num, ant, suc, dobro, triplo, raiz))