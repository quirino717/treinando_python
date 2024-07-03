import random

qtde = int(input('Quantas alunos há na turma? '))

nomes = []

print()

for i in range(1, qtde+1):
    nomes.append(str(input('Informe o nome do {}° aluno: ' .format(i))))

print()
sorteio = random.shuffle(nomes)

print('{}\n' .format(nomes))

for i in range(1, qtde+1):
    escolhido = nomes.pop(0)
    print('O {}° aluno a apresentar será {}'.format(i, escolhido))


