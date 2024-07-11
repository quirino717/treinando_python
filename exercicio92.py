from datetime import date

dicionario = {}

dicionario['Nome'] = str(input('Qual o nome: ')).capitalize()
dicionario['Nascido em'] = int(input(f'Qual ano {dicionario["Nome"]} nasceu: '))
dicionario['CTPS:'] = int(input('Número da carteira de trabalho (0 para não tem): '))

if dicionario['CTPS:'] != 0:
    dicionario['Contradado em'] = int(input('Qual foi o ano de contratação: '))
    dicionario['Ganha R$'] = float(input(f'O quanto {dicionario["Nome"]} ganha: R$'))
    dicionario['Se aponsentará com'] = ((dicionario["Contradado em"] + 35) - date.today().year) + (date.today().year - dicionario['Nascido em'])

print()
for c, v in dicionario.items():
    print(f'{c} {v}')