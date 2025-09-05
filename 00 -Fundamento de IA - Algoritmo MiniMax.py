
"""
O Algoritmo MiniMax é um método de busca em árvore que determina a estratégia ótima para um jogador em um jogo de soma zero com informação perfeita, assumindo que ambos os jogadores jogam de forma racional
Um jogo é chamado de soma zero quando o ganho de um jogador é exatamente a perda do outro, por exemplo, Se eu ganho +1 ponto, você automaticamente perde −1 ponto.
"""

import math

# Representação inicial do tabuleiro
# Índices: 0 1 2
#          3 4 5
#          6 7 8
tabuleiro = [" " for _ in range(9)]

def mostrar_tabuleiro():
    """Exibe o tabuleiro em formato 3x3"""
    for i in range(3):
        print(tabuleiro[3*i:3*(i+1)])
    print()

def movimentos_validos(tab):
    """Retorna as posições livres no tabuleiro"""
    return [i for i, v in enumerate(tab) if v == " "]

def verificar_vencedor(tab):
    """Verifica se há um vencedor ou empate"""
    combinacoes = [
        (0,1,2),(3,4,5),(6,7,8),  # linhas
        (0,3,6),(1,4,7),(2,5,8),  # colunas
        (0,4,8),(2,4,6)           # diagonais
    ]
    for (x,y,z) in combinacoes:
        if tab[x] == tab[y] == tab[z] != " ":
            return tab[x]  # retorna 'X' ou 'O'
    if " " not in tab:
        return "Empate"
    return None  # jogo ainda em andamento

def minimax(tab, profundidade, maximizando):
    """
    Implementação do algoritmo Minimax.
    maximizando = True -> turno da IA (O)
    maximizando = False -> turno do jogador humano (X)
    """
    vencedor = verificar_vencedor(tab)

    # Valores de utilidade (heurística simples)
    if vencedor == "O":  # IA vence
        return 1
    elif vencedor == "X":  # Humano vence
        return -1
    elif vencedor == "Empate":
        return 0

    if maximizando:
        melhor_valor = -math.inf
        for movimento in movimentos_validos(tab):
            tab[movimento] = "O"
            valor = minimax(tab, profundidade+1, False)
            tab[movimento] = " "
            melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        melhor_valor = math.inf
        for movimento in movimentos_validos(tab):
            tab[movimento] = "X"
            valor = minimax(tab, profundidade+1, True)
            tab[movimento] = " "
            melhor_valor = min(melhor_valor, valor)
        return melhor_valor

def melhor_jogada(tab):
    """Escolhe a melhor jogada para a IA (O) usando Minimax"""
    melhor_valor = -math.inf
    movimento_escolhido = None
    for movimento in movimentos_validos(tab):
        tab[movimento] = "O"
        valor = minimax(tab, 0, False)
        tab[movimento] = " "
        if valor > melhor_valor:
            melhor_valor = valor
            movimento_escolhido = movimento
    return movimento_escolhido

# Loop do jogo humano (X) vs IA (O)
def jogar():
    print("Bem-vindo ao Jogo da Velha com Minimax!")
    mostrar_tabuleiro()

    while True:
        # Jogador humano
        movimento = int(input("Sua jogada (0-8): "))
        if tabuleiro[movimento] != " ":
            print("Movimento inválido! Tente de novo.")
            continue
        tabuleiro[movimento] = "X"
        mostrar_tabuleiro()

        if verificar_vencedor(tabuleiro):
            print("Resultado:", verificar_vencedor(tabuleiro))
            break

        # Jogada da IA
        movimento_ia = melhor_jogada(tabuleiro)
        tabuleiro[movimento_ia] = "O"
        print(f"IA joga na posição {movimento_ia}")
        mostrar_tabuleiro()

        if verificar_vencedor(tabuleiro):
            print("Resultado:", verificar_vencedor(tabuleiro))
            break

# Executar o jogo
if __name__ == "__main__":
    jogar()
