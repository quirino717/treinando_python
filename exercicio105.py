def notas(*n, sit=False):
    """
    ->Função para analisar desempenho de uma turma
    :param n: as notas dos alunos
    :param sit: mostra um feedback baseado na média da turma
    :return: dicionário com as informações da turma
    """

    dicionario = {}
    dicionario['Total'] = len(n)
    dicionario['Maior nota'] = max(n)
    dicionario['Menor nota'] = min(n)
    dicionario['Média'] = sum(n)/len(n)

    if sit:
        if dicionario['Média'] < 5:
            dicionario['Situação'] = 'Ruim'
        elif dicionario['Média'] >= 7:
            dicionario['Situação'] = 'Poderia ser melhor'
        else:
            dicionario['Situação'] = 'Bom'

    return dicionario


n = notas(5.5, 2.5, 1.5, sit=True)
print(n)
help(notas)
