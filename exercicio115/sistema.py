from exercicio115.lib.interface import *
from exercicio115.lib.arquivo import *
from time import sleep

arquivo = 'cadastros.txt'
if not arquivoExiste(arquivo):
    criaArquivo(arquivo)

while True:
    escolha = menu(['Realizar cadastro', 'Checar cadastros', 'Encerrar o programa'])

    if escolha == 1:
        titulo('Área de casdastros')
        nome = str(input('Informe o nome: ')).strip().title()
        idade = inteiro('Informe a idade: ')

        cadastrar(arquivo, nome, idade)

    elif escolha == 2:
        leArquivo(arquivo)

    elif escolha == 3:
        sair()
        break
    else:
        print('\n\033[1;31mPor favor, digite uma opção válida\033[m')
    sleep(1)
