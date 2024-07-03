num = float(input('Digite um número: '))

print('\nA tabuada do número {} é:\n' .format(num))
print('-'*20)
for i in range(1, 11):
    print('{} x {} = {}' .format(num, i, (num*i)))
print('-'*20)