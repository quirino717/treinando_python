qtde = 0
soma = 0

for i in range (1, 501, 2):
    if i % 3 == 0:
        qtde += 1
        soma += i
print('A soma de todos os {} números múltiplos de 3'
      '\nno intervalo de 1 e 500 é: {}' .format(qtde, soma))