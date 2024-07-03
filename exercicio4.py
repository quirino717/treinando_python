algo = input('Digite algo: ')

print('\nO tipo primitivo desse valor é {}' .format(type(algo)))
print('Só tem espaços? Resposta: {}' .format(algo.isspace()))
print('É um número? Resposta: {}' .format(algo.isnumeric()))
print('É alfabético? Resposta: {}' .format(algo.isalpha()))
print('É alfanumérico? Resposta: {}' .format(algo.isalnum()))

if algo.isalpha():
    print('É tudo maiúsculo? Resposta: {}' .format(algo.isupper()))
    print('É tudo minúsculo? Resposta: {}' .format(algo.islower()))
    print('É tudo capitalizado? Resposta: {}' .format(algo.istitle()))