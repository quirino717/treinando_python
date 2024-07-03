dia = input('informe o dia de hoje: ')
if dia.isnumeric():
    dia = int(dia)
    print('Hoje é dia {}' .format(dia))
else:
    print('O valor a ser digitado deve ser um número')
