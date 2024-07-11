lista = []

while True:
    nome = (str(input('\nNome: ')).title())
    nota1 = (int(input('1° nota: ')))
    nota2 = (int(input('2° nota: ')))
    media = (nota1 + nota2) / 2

    lista.append([nome, [nota1, nota2], media])

    escolha = str(input('Quer adicionar mais um aluno? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Resposta inválida...')
        escolha = str(input('Quer adicionar mais um aluno? [S/N] ')).strip().upper()[0]

    if escolha == 'N':
        break

print('\n' + '\033[1m-=' * 20)
print('{:^40}'.format("Boletim"))
print('\033[1m-=\033[m' * 20 + '\n')

print(f'{"N°":<3}{"Aluno":<8}{"Média":>29}')
print(f'\033[4m-\033[m' * 40)

for i, j in enumerate(lista):
    print(f'{i + 1 :<3}{j[0]:<8}\033[32m{j[2]:>29}\033[m' if j[2] >= 5 else f'{i + 1 :<3}{j[0]:<8}\033[31m{j[2]:>29}\033[m')
print(f'\033[4m-\033[m' * 40)

while True:
    aluno = int(input('\nDigite o N° do aluno para ver as notas (999 encerra): '))

    if aluno != 999:
        print(f'As notas de \033[4m{lista[aluno - 1][0]}\033[m são: \033[1m{lista[aluno - 1][1]}\033[m')
    else:
        print()
        print(f'{"FIM":^40}')
        break
