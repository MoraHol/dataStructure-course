from random import randint


def inicializacionMatriz(m): ##inicializa la matriz en 0 con el tamaño m
    matriz = []
    for x in range(0, m):
        matriz.append([0] * m)

    return matriz

def RomboImpares(matriz,m): ## funcion para guardar los valores del interio de un rombo con tamaño impar
    k = int(matriz.__len__() / 2)
    u = k - 1

    matriz2 = inicializacionMatriz(m) ##inicializando la matriz para alojar las posiciones dentro del rombo
    ## dvidir matriz en 4 y sacando daigonales
    for i in range(0,k):## aloja la diagonal superior izquerda
        for j in range(u+1,k):
            matriz2[i][j] = matriz[i][j]
        u -= 1

    u = 0
    for i in range(k,matriz.__len__()): ##aloja la diagonal inferior izquierda
        for j in range(u,k):
            matriz2[i][j] = matriz[i][j]
        u += 1

    u = k + 1
    for i in range(0,k): ## aloja la diagonal superior derecha
        for j in range(k,u):
            matriz2[i][j] = matriz[i][j]
        u += 1

    u = matriz.__len__()
    for i in range(k,matriz.__len__()): ##aloja la diagonal inferior derecha
        for j in range(k,u):
            matriz2[i][j] = matriz[i][j]
        u -= 1

    return matriz2

def RomboPares(matriz, m): ## funcion para guardar los valores del interior de un rombo con tamaño par
    k = int(matriz.__len__() / 2)
    u = k - 1

    matriz2 = inicializacionMatriz(m) ## inicializando la matriz para alojar las pocisiones del rombo

    for i in range(0, k): ## aloja la diagonal superior izquierda
        for j in range(u, k):
            matriz2[i][j] = matriz[i][j]

        u -= 1
    u = 0
    for i in range(k, matriz.__len__()): ##aloja la diagonal inferior izquierda
        for j in range(u, k):
            matriz2[i][j] = matriz[i][j]
        u += 1
    u = k + 1
    for i in range(0, k): ## aloja la diagonal superior derecha
        for j in range(k, u):
            matriz2[i][j] = matriz[i][j]
        u += 1
    u = matriz.__len__()

    for i in range(k, matriz.__len__()): ## aloja la diagonal inferior derecha
        for j in range(k, u):
            matriz2[i][j] = matriz[i][j]
        u -= 1
    return matriz2


def MostrarMatriz(matriz): ## funcion para imprimir matriz de forma mas presentable
    matriz3 = []
    for i in range(0, matriz.__len__()):
        for j in range(0, matriz.__len__()):
            matriz3.append(matriz[i][j])
        print(matriz3)
        matriz3 = []
def llenadoMatrizAleaotrio(matriz,m):
    ##lleando aleatorio de matriz
    for i in range(m):
        for j in range(m):
            matriz[i][j] = randint(1, 9)
    return matriz
class ImpresionInteriorRombo(): ## clase principal
    m = int(input("Introduce el valor de m: "))
    print(m)
    matriz = inicializacionMatriz(m)

    matriz = llenadoMatrizAleaotrio(matriz,m)



    if (m % 2 == 0):
        matriz2 = RomboPares(matriz, m)
    else:
        matriz2 = RomboImpares(matriz,m)

    MostrarMatriz(matriz)
    print()
    MostrarMatriz(matriz2)
