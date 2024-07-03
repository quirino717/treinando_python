soma = 0
qtde = 0

x = int(input('Informe até qual número irá a somatória: '))
print('')

for i in range(1, (x + 1)):
    num = int(input('Digite o {}° número para a soma: ' .format(i)))
    qtde += 1
    if num % 2 == 0:
        soma += num

print('\nNo intervalo de 1 até {}, há {} valores pares'
      '\ne a somatória deles é igual a: {} ' .format(x, qtde, soma))