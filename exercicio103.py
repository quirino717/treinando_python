def ficha(nome='<desconhecido>', gols=0):
    print(f'\nO jogador \033[1m{nome}\033[m marcou \033[1m{gols}\033[m gol(s)' if gols != 0 else f'\nO jogador \033[1m{nome} \033[31mnão marcou gols\033[m')


print('-' * 40)
n = str(input('Nome do jogador: ')).strip().title()
g = str(input('Gols marcados: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
