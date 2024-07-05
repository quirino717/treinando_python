entrada = str(input('Informe o seu sexo: ')).upper().strip()

while entrada not in 'MmFf':
    print('\nDados inválidos')
    entrada = str(input('Por favor, informe novamente: ')).upper().strip()

print('Adicionado!')
