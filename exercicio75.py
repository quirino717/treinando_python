tupla = (int(input('Digite um número: ')), int(input('Digite um outro número: ')), int(input('Digite um outro número: ')),
         int(input('Digite um outro número: ')), int(input('Digite um outro número: ')))

print(f'\nOs valores digitados foram {tupla}')

print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O número 3 apareceu na {tupla.index(3) + 1}° posição')
else:
    print('O número 3 não aparece')

print('Os valores pares digitados foram: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(f'{i}', end=' ')
