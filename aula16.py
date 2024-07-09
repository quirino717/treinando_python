palavra = 'cachorro'
contador = 0
palpite = ''
chutes = []

while True:

    for i in palavra:
        if i in chutes:
            print(i, end='')
        else:
            print('_', end='')

    palpite = str(input('\nPalpite: '))

    if palpite in chutes:
        print('Já tentou essa letra')
        palpite = str(input('\nPalpite: '))

    chutes.append(palpite)
    contador = 0

    for i in palavra:
        if i in chutes:
            contador += 1

    if contador == len(palavra):
        print(palavra)
        print('Você venceu!!')
        break
