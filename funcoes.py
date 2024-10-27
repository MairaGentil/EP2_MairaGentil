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

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = [
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10
    ]
    for embarcacoes in frota:
        for posicoes in frota[embarcacoes]:
            for posicao in posicoes:
                linha, coluna = posicao
                tabuleiro[linha][coluna] = 1
    return tabuleiro

def afundados(frota, tabuleiro):
    qnt_afundados = 0
    for embarcacao in frota:
        for posicoes in frota[embarcacao]:
            pmarcadas = 0
            for linha, coluna in posicoes:
                if tabuleiro[linha][coluna] == 'X':
                    pmarcadas += 1
            if pmarcadas == len(posicoes):
                qnt_afundados += 1
    return qnt_afundados

    # for linhas in tabuleiro:
    #     for p in linhas:
    #         if linhas[p] == 'x':
    #             qnt_afundados += 1

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    ocupadas = 0
    for valor in frota.values():
        for listavalores in valor:
            for parfrota in listavalores:
                for par in posicoes:
                    if par == parfrota:
                        ocupadas += 1
    for par in posicoes:
        if 9 < par[0] or par[0] < 0:
            ocupadas += 1
        if 9 < par[1] or par[1] < 0:
            ocupadas += 1
    if ocupadas  == 0:
        return True 
    else:
        return False
