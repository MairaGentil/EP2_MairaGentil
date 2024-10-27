from funcoes import *

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
print(frotav)