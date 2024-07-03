import emoji
from time import sleep

print('Os fogos começarão em...\n')

for i in range(10, 0, -1):
    print('{:^20}'.format(i))
    sleep(1)

print('{:^20}' .format('BOOOOOOOOOM'))
print(emoji.emojize(':fireworks:')*8)