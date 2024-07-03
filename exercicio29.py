print('-='*23, '\n\tAtenção! Você está dirigindo em uma rua\n\t'
               'cujo limite é 80km/h\n' + '-='*23)

vel = float(input('\n\tQual a velocidade que você passou por ela? '))

if vel > 80:
    print('\n\033[1;31mVocê foi multado!!!\033[m\nVocê estava {}km/h acima do limite permitido\n'
          'Você deverá pagar uma multa de R${:.2f}'
          .format((vel - 80), (vel - 80) * 7))
else:
    print('\nVocê é um motorista consciente!!\nContinue assim')