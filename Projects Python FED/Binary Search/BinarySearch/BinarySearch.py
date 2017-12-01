def BinarySearch(array, x):
    """

    :param array: recibe el arreglo ordenado
    :param x: recibe el numero a buscar dentro del arreglo
    :return: la posición en la que esta el numero en el arreglo
    """
    lowerBound = 0
    upperBound = array.__len__() - 1
    index = -1
    'si el limite superior es el mismo que el inferior, entonces no hay solución factible'
    while lowerBound < upperBound:
        middlePoint = int((lowerBound + upperBound) / 2)
        if x == array[middlePoint]:
            # x ha sido encontrado
            index = middlePoint
            break
        else:

            if x < array[middlePoint]:
                upperBound = middlePoint - 1
            else:
                lowerBound = middlePoint + 1
    # cuando el limite inferior y el superior sean iguales es ahi donde estará
    # la posición de x
    if lowerBound == upperBound and array[lowerBound] == x:
        index = lowerBound

    return index


class main:
    line = input("ingrese los elementos ordenados y separados por coma: \n")
    matInput = line.split(",")
    array = []

    # llenado de arreglo
    for i in range(0, matInput.__len__()):
        array.append(int(matInput[i]))

    # número a buscar
    x = int(input("ingrese el numero a buscar: \n"))

    # llamado de la función
    index = BinarySearch(array, x)
    print("el número esta en la posición ", (index + 1), " del arreglo")
