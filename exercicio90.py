dicionario = {}

dicionario['Nome'] = str(input('Qual o nome do aluno: ')).capitalize()
dicionario['Média'] = float(input(f'Qual a média de {dicionario["Nome"]}: '))

'''print(f'\nO aluno {dicionario["Nome"]}')
print(f'Tem a média igual a {dicionario["Média"]:.2f}')
print(f'O que siginifica que ele está \033[32maprovado\033[m' if dicionario["Média"] > 5 else f'O que siginifica que ele está \033[31mreprovado\033[m')
'''

if dicionario["Média"] > 5:
    dicionario['Situação'] = 'aprovado'
else:
    dicionario['Situação'] = 'reprovado'

print()

for c, v in dicionario.items():
    print(f'{c} é igual a: {v}')
