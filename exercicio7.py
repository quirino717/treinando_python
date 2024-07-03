notas = []
qtde = int(input('Deseja calcular a média de quantas notas? '))

print('')

for i in range(1, qtde+1):
    notas.append(float(input('Digite a {}° nota: ' .format(i))))

media = sum(notas)/len(notas)

print('\nA média do aluno é de: {:.1f}' .format(media))

if media >= 5:
    print('\nAluno aprovado!')
else:
    print('\nAluno reprovado!')