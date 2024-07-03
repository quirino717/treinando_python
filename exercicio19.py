import random

qtde = int(input('Quantas alunos há na turma? '))

nomes = []

print()

for i in range(1,qtde+1):
    nomes.append(str(input('Informe o nome do {}° aluno: ' .format(i))))

escolha = random.choice(nomes)

print('\nO aluno escolhido foi {}'.format(escolha))