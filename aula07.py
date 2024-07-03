nome = input('Digite seu nome: ')
print('Prazer em te conhecer, {:-^20}!\n'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
divi = n1 // n2
e = n1 ** n2

print('\nA soma vale: {}\nA subtração vale: {}\nA multiplicação vale: {}\nA divisão vale: {:.3f}\nA divisão inteira vale: {}\nA potência vale: {}\n' .format(soma, sub, mul, div, divi, e))