sal = float(input('\n\tInforme o seu salário: R$'))

if sal <= 1250:
    print('\n\tVocê recebeu um aumento de 15%\n\t'
          'Seu salário agora é de \033[1;32mR${:.2f}' .format(sal + (sal * 0.15)))
else:
    print('\n\tVocê recebeu um aumento de 10%\n\t'
          'Seu salário agora é de \033[1;32mR${:.2f}'.format(sal + (sal * 0.1)))