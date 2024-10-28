from funcoes import *
import random 
random.seed(2)

nom= {"porta-aviões":[4,1], "navio-tanque":[3,2], "contratorpedeiro":[2,3], "submarino":[1,4]}
# [tamanho,quantidade]

frotav = {"porta-aviões":[], "navio-tanque":[],"contratorpedeiro":[],"submarino":[]}

for nome,(tamanho,qnt) in nom.items():
    for i in range(qnt):
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        linha = int(input("linha: "))
        coluna = int(input("coluna: "))
        if nome != 'submarino':
            orientacao = int(input("[1] Vertical [2] Horizontal >"))
            if orientacao == 1:
                orientacao = 'vertical'

            elif orientacao == 2:
                orientacao = 'horizontal'

        verificacao = posicao_valida(frotav, linha, coluna, orientacao, tamanho)

        if verificacao == False:
            print("Esta posição não está válida!")
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        while verificacao == False:
            linha = int(input("linha: "))
            coluna = int(input("coluna: "))
            if nome != 'submarino':
                orientacao = int(input("[1] Vertical [2] Horizontal >"))
                if orientacao == 1:
                    orientacao = 'vertical'
                elif orientacao == 2:
                    orientacao = 'horizontal'
            verificacao = posicao_valida(frotav, linha, coluna, orientacao, tamanho)
            if verificacao == False:
                print("Esta posição não está válida!")
                print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}") 

        p_definidas = define_posicoes(linha, coluna, orientacao, tamanho)
        prefrota = preenche_frota(frotav,nome,linha,coluna,orientacao,tamanho)
# print(frotav)

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

taboponente = posiciona_frota(frota_oponente)
tabjogador = posiciona_frota(frotav)

print(monta_tabuleiros(tabjogador,taboponente))

jogando = True
jogadas_feitas = []
jogadas_oponentes = []

while jogando == True:
    valida = - 1
    while valida == -1:
        linha = int(input('Jogador, qual linha deseja atacar? '))
        quebra = 0
        if linha < 0 or linha > 9:
            print('Linha inválida!')
            quebra = -1
        while quebra == -1:
            linha = int(input('Jogador, qual linha deseja atacar? '))
            quebra = 0
            if linha < 0 or linha > 9:
                print('Linha inválida!')
                quebra = -1
        
        coluna = int(input('Jogador, qual coluna deseja atacar? '))
        quebra = 0
        if coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            quebra = -1
        while quebra == -1:
            coluna = int(input('Jogador, qual coluna deseja atacar? '))
            quebra = 0
            if coluna < 0 or coluna > 9:
                print('Coluna inválida!')
                quebra = -1
        jogado = [linha,coluna]
        if jogado not in jogadas_feitas:
            jogadas_feitas.append(jogado)
            valida = 0
        else:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')

    taboponente = faz_jogada(taboponente,linha,coluna)
    quantidade_afundados = afundados(frota_oponente,taboponente)

    if quantidade_afundados == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

