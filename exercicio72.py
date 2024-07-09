nums = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    num = int(input('\nDigite um número de 0 a 20: '))

    if 0 <= num <= 20:
        print(f'\nVocê digitou o número \033[1;4m{nums[num]}\033[m')
        continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]

        while continuar not in 'SN':
            print('Opção inválida, tente novamente!')
            continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]

        if continuar in 'Nn':
            break
    else:
        print('Opção inválida, tente novamente!')