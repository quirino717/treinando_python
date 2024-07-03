num = int(input('Digite o número que você deseja saber a tabuada: '))
tabuada = int(input('Até qual valor deseja que a tabuada vá? '))

print('\nA tabuada do número {} é:\n' .format(num))
print('-'*20)

for i in range (1, tabuada+1):
    print('{} x {} = \033[1m{}\033[m' .format(num, i, num*i))

print('-'*20)
