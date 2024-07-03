print('\033[34m-='*20)
print('{: ^40}' .format("Quirino's Store"))
print('\033[34m-=\033[m'*20)

valor = float(input('\n\tQual foi o valor da sua compra? R$'))

print('\n\tQual será a forma de pagamento?'
      '\n\tDigite 1 para pagamento a vista'
      '\n\tDigite 2 para pagamento no cartão de débito'
      '\n\tDigite 3 para parcelar 2x no cartão'
      '\n\tDigite 4 para parcelar 3x ou mais')

escolha = int(input('\n\tO que deseja fazer: '))

if escolha == 1:
    print('\n\tPor pagar a vista, você recebará 10% de desconto'
          '\n\tEntão deverá pagar R${:.2f}' .format(valor - (valor * 0.10)))
elif escolha == 2:
    print('\n\tPor pagar no débito, você recebará 5% de desconto'
          '\n\tEntão deverá pagar R${:.2f}'
          '\n\tÉ só inserir ou aproximar'.format(valor - (valor * 0.05)))
elif escolha == 3:
    print('\n\tSua compra será feita em duas parcelas de R${:.2f}'
          '\n\tÉ só inserir ou aproximar' .format(valor / 2))
elif escolha == 4:
    qtde = int(input('\n\tEm quantas vezes deseja parcelar? '))
    total = valor + (valor * 0.2)
    parcelas = total/qtde
    print('\n\tDevido aos juros, o valor total será de R${:.2f}'
          '\n\tSerão feitas {} parcelas de R${:.2f}'
          '\n\tÉ só inserir ou aproximar' .format(total, qtde, parcelas))
else:
    print('\n\tOpção inválida')