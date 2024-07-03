nome = str(input('Informe seu nome completo: ')).strip().upper()

x = nome.find(' SILVA')

if x != -1:
    print('\nVocê é um Silva!')
elif nome[:5] == 'SILVA':
    print('\nVocê se chama Silva, mas não é da família Silva')
else:
    print('\nVocê não é um Silva')