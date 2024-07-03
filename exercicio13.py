salario = float(input('Valor do salário: R$'))
aumento = float(input('Porcentagem do aumento: '))

final = salario + salario*(aumento/100)

print('\nApós um aumento de {}% o seu salário foi de R${} para R${:.2f}'.format(aumento, salario, final))