import time
import random


matriz = [
    [6, 3, 1, 1, 2, 2, 3, 1],
    [6, 4, 6, 3, 4, 2, 4, 1],
    [3, 2, 4, 2, 4, 5, 2, 3],
    [2, 4, 4, 4, 2, 1, 2, 3],
    [1, 2, 3, 4, 2, 2, 2, 5],
    [5, 5, 4, 4, 5, 1, 5, 5],
    [3, 3, 4, 4, 3, 4, 2, 2],
    [1, 2, 3, 6, 2, 4, 1, 2]
]


movimentos = {
    'cima': (-1, 0), #cada direção equivale a uma tupla
    'baixo': (1, 0),
    'esquerda': (0, -1),
    'direita': (0, 1),
    'diag_cima_direita': (-1, 1),
    'diag_baixo_esquerda': (1, -1)
} #dicionário

# direcao = 'cima'
# movimento = movimentos[direcao]  # Isto vai retornar (-1, 0)

# novo_i = i + movimento[0]  # Atualiza a coordenada i
# novo_j = j + movimento[1]  # Atualiza a coordenada j

def imprimir_matriz(matriz, pos_atual):
    for i in range(len(matriz)):
        linha = ""
        for j in range(len(matriz[i])):
            if (i, j) == pos_atual:
                linha += f"[*{matriz[i][j]}*] "
            else:
                linha += f"[{matriz[i][j]}] "
        print(linha)
    print("\n")

def mover(matriz, pos, direcoes_fixas, tentativa_num):
    i, j = pos
    dado = matriz[i][j] #dadao atual current focus

    if (i == 0 and j == 7):
        print(f"Caminho encontrado ao (0, 7)!")
        return True

    imprimir_matriz(matriz, pos)
    time.sleep(1)

    if dado in direcoes_fixas: #se od ados existir
        direcao = direcoes_fixas[dado] # a direção é a chave dado, nesse primeior caso que vale o valor na posiçao (0, 7), que é 1
        di, dj = movimentos[direcao] #(-1, 0)
        novo_i = i + di * dado
        novo_j = j + dj * dado

        if 0 <= novo_i < 8 and 0 <= novo_j < 8:
            print(f"Tentativa {tentativa_num}: Mover de ({i}, {j}) para ({novo_i}, {novo_j}) com dado {dado} na direção '{direcao}'")
            if mover(matriz, (novo_i, novo_j), direcoes_fixas, tentativa_num):
                return True
        else:
            print(f"Tentativa de mover de ({i}, {j}) para fora da matriz em ({novo_i}, {novo_j})")
            print(f"================= Nova Tentativa {tentativa_num} =================")
            return False

    return False

def encontrar_caminhos(matriz):
    tentativa_num = 0

    while True:
        tentativa_num += 1
        print(f"================= Nova Tentativa {tentativa_num} =================")

        # Cria direções aleatórias
        direcoes_fixas = {1: 'cima', 2: 'baixo', 3: 'esquerda', 4: 'direita', 5: 'diag_cima_direita', 6: 'diag_baixo_esquerda'}
        direcoes_fixas = dict(zip(direcoes_fixas.keys(), random.sample(list(direcoes_fixas.values()), len(direcoes_fixas))))

        imprimir_legenda(direcoes_fixas)

        if mover(matriz, (7, 0), direcoes_fixas, tentativa_num):
            break

def imprimir_legenda(direcoes_fixas):
    print("Legenda das Direções:")
    for dado, direcao in direcoes_fixas.items():
        print(f"{dado}: {direcao}")
    print("\n")

encontrar_caminhos(matriz)
