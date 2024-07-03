casa = float(input('\n\tQual o valor da casa que deseja comprar? R$'))
sal = float(input('\tQual o valor do seu salário? R$'))
anos = int(input('\tEm quantos anos deseja pagar a casa? '))

prestacao = casa / (anos * 12)

print('\n\tPara pagar uma casa de R${:.2f} em {} anos\n\t'
      'as prestações serão de R${:.2f} por mês' .format(casa, anos, prestacao))

if prestacao <= (sal * 0.3):
    print('\n\tEntão, o emprestimo será \033[1;32maprovado!\033[m')
else:
    print('\n\tEntão, o emprestimo será \033[1;31mnegado!\033[m')