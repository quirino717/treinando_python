num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

escolha = ''

while escolha != 0:
    print('\nO que deseja fazer com esses números?'
          '\nDigite \033[1;4m1\033[m para somar'
          '\nDigite \033[1;4m2\033[m para subtrair'
          '\nDigite \033[1;4m3\033[m para multiplicar'
          '\nDigite \033[1;4m4\033[m para dividir'
          '\nDigite \033[1;4m5\033[m para mudar os números'
          '\nDigite \033[1;4m0\033[m para sair')

    escolha = int(input('\nDigite sua escolha: '))

    if escolha == 1:
        print('\nExibindo resultado da soma\n{} + {} = {}'.format(num1, num2, num1 + num2))

    if escolha == 2:
        print('\nExibindo resultado da subtração\n{} - {} = {}'.format(num1, num2, num1 - num2))

    if escolha == 3:
        print('\nExibindo resultado da multiplicação\n{} x {} = {}'.format(num1, num2, num1 * num2))

    if escolha == 4:
        print('\nExibindo resultado da divisão\n{} / {} = {}'.format(num1, num2, num1 / num2))

    if escolha == 5:
        num1 = int(input('\nDigite um novo número: '))
        num2 = int(input('Digite outro novo número: '))

    if escolha == 0:
        break

print('\nEncerrando')
