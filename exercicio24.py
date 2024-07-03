cidade = str(input('Digite o nome da sua cidade: ')).strip()

checa = cidade.capitalize()

x = checa.find('Santo')

if x != -1:
    print('\nA sua cidade possui Santo em seu nome!')
else:
    print('\nA sua cidade não possui Santo em seu nome!')