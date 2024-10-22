def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    if orientacao == 'vertical':
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])

    elif orientacao == 'horizontal':
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])

    return posicoes


def preenche_frota(frota,nome,linha,coluna,orientacao,tamanho):
    posicao = define_posicoes(linha,coluna,orientacao,tamanho)
    if nome in frota:
        frota[nome].append(posicao)
    else:
        frota[nome] = [posicao]
    return frota
