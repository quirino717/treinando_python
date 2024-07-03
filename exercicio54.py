from datetime import date

qtde = int(input('\nDeseja analisar a idade de quantas pessoas? '))
contador = 0

velho = novo = pessoanova = pessoavelha = 0

print('')

for i in range(1, qtde+1):
    ano = int(input('Informe o ano de nascimento da {}° pessoa: '.format(i)))
    print('\tEssa pessoa tem {} anos' .format(date.today().year - ano))
    idade = date.today().year - ano

    if idade < 18:
        contador += 1

    if i == 1:
        velho = novo = idade
        pessoanova = pessoavelha = i
    else:
        if idade > velho:
            velho = idade
            pessoavelha = i
        if idade < novo:
            novo = idade
            pessoanova = i

print('\nDessas pessoas, {} são maiores e {} são menores' .format(qtde - contador, contador))
print('A {}° pessoa é a mais velha e tem {} anos'
      '\nA {}° pessoa é a mais nova e tem {} anos' .format(pessoavelha, velho, pessoanova, novo))