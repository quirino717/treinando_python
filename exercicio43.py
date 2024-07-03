print('\033[34m-='*20)
print('{:^40}'.format('Venha calcular o seu IMC'))
print('\033[34m-=\033[m'*20)

altura = float(input('\n\tInforme a sua altura: '))
peso = float(input('\tInforme o seu peso: '))

imc = peso / (altura * altura)

print('\n\tSeu Índice de Massa Corpórea é de {:.2f}kg/m²' .format(imc))
print('\tO que significa que você está ', end='')

if imc < 18.5:
    print('\033[1;4mabaixo do peso')
    print('\n\tVocê precisa ganhar {}')
elif imc < 25:
    print('no \033[1;4mpeso ideal')
elif imc < 30:
    print('em \033[1;4msobrepeso')
elif imc < 40:
    print('\033[1;4mobeso')
else:
    print('em \033[1;4mobesidade mórbida')