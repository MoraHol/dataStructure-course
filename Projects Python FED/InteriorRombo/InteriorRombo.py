from random import randint


def InicializacionMatriz(m):
    """
    inicializa la matriz en 0 con el tamaño m
    :param m: tamaño de la matriz
    :return: la matriz en 0
    """
    matriz = []
    for x in range(0, m):
        matriz.append([0] * m)

    return matriz


def RomboImpares(matriz, m):
    """
    función para guardar los valores del interior de un rombo con tamaño impar
    :param matriz: es la matriz de donde se escogerán los números
    :param m: es el tamaño de la matriz
    :return: una matriz que solo tiene los números que conforman el interior de un rombo impar
    """
    k = int(matriz.__len__() / 2)
    u = k - 1
    # inicializando la matriz para alojar las posiciones dentro del rombo
    matriz2 = InicializacionMatriz(m)
    # dividir matriz en 4 nuevas matrices y sacando diagonales
    for i in range(0, k):  # aloja la diagonal superior izquierda
        for j in range(u + 1, k):
            matriz2[i][j] = matriz[i][j]
        u -= 1

    u = 0
    for i in range(k, matriz.__len__()):  # aloja la diagonal inferior izquierda
        for j in range(u, k):
            matriz2[i][j] = matriz[i][j]
        u += 1

    u = k + 1
    for i in range(0, k):  # aloja la diagonal superior derecha
        for j in range(k, u):
            matriz2[i][j] = matriz[i][j]
        u += 1

    u = matriz.__len__()
    for i in range(k, matriz.__len__()):  # aloja la diagonal inferior derecha
        for j in range(k, u):
            matriz2[i][j] = matriz[i][j]
        u -= 1

    return matriz2


def RomboPares(matriz, m):
    """
    función para guardar los valores del interior de un rombo con tamaño par
    :param matriz: es la matriz de donde se escogerán los números
    :param m: es el tamaño de la matriz
    :return: una matriz que solo tiene los números que conforman el interior de un rombo par
    """

    k = int(matriz.__len__() / 2)
    u = k - 1
    # inicializando la matriz para alojar las posiciones del rombo
    matriz2 = InicializacionMatriz(m)

    for i in range(0, k):  # aloja la diagonal superior izquierda
        for j in range(u, k):
            matriz2[i][j] = matriz[i][j]

        u -= 1
    u = 0
    for i in range(k, matriz.__len__()):  # aloja la diagonal inferior izquierda
        for j in range(u, k):
            matriz2[i][j] = matriz[i][j]
        u += 1
    u = k + 1
    for i in range(0, k):  # aloja la diagonal superior derecha
        for j in range(k, u):
            matriz2[i][j] = matriz[i][j]
        u += 1
    u = matriz.__len__()

    for i in range(k, matriz.__len__()):  # aloja la diagonal inferior derecha
        for j in range(k, u):
            matriz2[i][j] = matriz[i][j]
        u -= 1
    return matriz2


def MostrarMatriz(matriz):
    """
    función para imprimir matriz de forma mas presentable
    :param matriz: la cual se quiera ver en pantalla
    """
    Buffer = ""
    for i in range(0, matriz.__len__()):
        for j in range(0, matriz.__len__()):
            if matriz[i][j] == 0:
                Buffer += "  "
            else:
                Buffer += str(matriz[i][j]) + " "
        Buffer += "\n"
    print(Buffer)

def llenadoMatrizAleatorio(matriz, m):

    """
    llenado aleatorio de matriz
    :param matriz: contiene una matriz inicializada en cero
    :param m: el tamaño de la matriz
    :return: una matriz con números aleatorios de 1 a 9
    """
    for i in range(m):
        for j in range(m):
            matriz[i][j] = randint(1, 9)
    return matriz


class ImpresionInteriorRombo:  # clase principal
    m = int(input("Introduce el valor de m: "))
    print(m)
    matriz = InicializacionMatriz(m)

    matriz = llenadoMatrizAleatorio(matriz, m)

    if m % 2 == 0:
        matriz2 = RomboPares(matriz, m)
    else:
        matriz2 = RomboImpares(matriz, m)

    MostrarMatriz(matriz)
    print()
    MostrarMatriz(matriz2)
