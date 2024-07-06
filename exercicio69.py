print('\033[1;m-='*20)
print('{:^40}' .format('Cadastro'))
print('\033[1;m-=\033[m'*20)

cont = conth = contm = conti = 0

while True:
    idade = int(input('\n\tInforme a idade: '))
    sexo = str(input('\tInforme o sexo [M/F]: ')).strip().upper()[0]

    while sexo not in 'MF':
        print('\n\tOpção inválida')
        sexo = str(input('\tInforme o sexo [M/F]: ')).strip().upper()[0]

    if idade > 18:
        conti += 1

    if sexo == 'M':
        conth += 1

    if sexo == 'F' and idade < 20:
        contm += 1

    cont += 1

    escolha = str(input('\n\tDeseja cadastrar mais alguém (S/N): ')).strip().upper()[0]
    if escolha == 'N':
        break

print(f'\n\tForam cadastradas {cont} pessoas\n\t{conti} tem mais de 18 anos\n\t{conth} são homens\n\t{contm} são mulheres com menos de 20 anos')
