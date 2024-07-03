num = []

for i in range (1, 4):
    num.append(int(input('\tDigite o {}° número: ' .format(i))))

menor = num[0]
maior = num[0]

if num[1] < num[0] and num[1] < num[2]:
    menor = num[1]
if num[2] < num[0] and num[2] < num[1]:
    menor = num[2]

if num[1] > num[0] and num[1] > num[2]:
    maior = num[1]
if num[2] > num[0] and num[2] > num[1]:
    maior = num[2]

print('\n\tO menor valor entres os digitados é {}\n\t'
      'O maior valor entres os digitados é {}' .format(menor, maior))