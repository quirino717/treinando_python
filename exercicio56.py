from time import sleep

print('\033[1;35m-='*20)
print('{:^40}' .format('Analisador completo'))
print('\033[1;35m-=\033[m'*20)

qtde = int(input('\n\tQuantas pessoas deseja analiar? '))

velho = novo = contador = idadevelho = contmulher = conthomem = media = soma = 0
homemvelho = ''

print('')

for i in range(1, qtde + 1):
    nome = str(input('\tDigite o nome da {}° pessoa: ' .format(i))).upper().strip()
    idade = int(input('\tDigite a idade da {}° pessoa: ' .format(i)))
    sexo = str(input('\tDigite o sexo da {}° pessoa (M/F): ' .format(i))).upper().strip()
    print('')

    soma += idade

    if sexo == 'M':
        if i == 1:
            homemvelho = nome
            idadevelho = idade
        else:
            if idade > idadevelho:
                homemvelho = nome
                idadevelho = idade

    if sexo == 'F':
        contmulher += 1
        if idade < 20:
            contador += 1

print(' '*10 + '{}' .format('Analisando dados'), end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)

print('\n\tResultados da análise:\n\tA média de idade é de {}' .format(soma / qtde))

print('\t{} é o homem mais velho com {} anos' .format(homemvelho.capitalize(), idadevelho))

if contador == 1:
    print('\tApenas 1 mulher tem menos de 20 anos')
elif contador == 0:
    print('\tNenhuma mulher tem menos de 20 anos')
elif contador == contmulher:
    print('\tTodas as mulheres tem menos de 20 anos')
else:
    print('\tE apenas {} mulheres tem menos de 20 anos'.format(contador))

