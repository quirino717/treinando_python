expr = (str(input('Digite uma expressão matemática: '))).strip()
lista = list(expr)
verifica = 0

for i in lista:
    if i == '(':
        verifica += 1
    if i == ')':
        verifica -= 1

if verifica != 0:
    print('\nA expressão digitada está errada')
else:
    print('\nA expressão digitada está correta')
