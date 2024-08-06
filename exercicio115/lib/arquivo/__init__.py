from exercicio115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #rt = read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArquivo(nome):
    try:
        a = open(nome, 'wt+') #wt = write text
        a.close()
    except:
        print('\n\033[1;31mOcorreu um erro ao criar o arquivo!!\033[m')
    else:
        print(f'\nO arquivo {nome} foi criado com sucesso!!')


def leArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\n\033[1;31mOcorreu um erro ao ler o arquivo!!\033[m')
    else:
        titulo('Pessoas cadastradas')

        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')

            print(f'Nome: \033[1m{dado[0]:<30}\033[m Idade:\033[1m{dado[1]:>3} anos\033[m')

    finally:
        print(a.read())


def cadastrar(arquivo, nome = '', idade = 0):
    try:
        a = open(arquivo, 'at') #at = append text
    except:
        print('\n\033[1;31mOcorreu um erro ao abrir o arquivo!!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\n\033[1;31mOcorreu um erro ao cadastrar os dados!!\033[m')
        else:
            print(f'\n{nome} foi cadastrado com sucesso!!')
            a.close()
