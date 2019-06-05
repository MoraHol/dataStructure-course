def InterpolationSearch(array, x):
    """
    parecido BinarySearch solo que este método va directamente al índice
    :param array: el arreglo de números y tiene que estar ordenado
    :param x: es el numero el cual se va a buscar en el arreglo
    :return: el índice de numero que se esta buscando
    """
    lowerBound = 0
    upperBound = array.__len__() - 1
    index = -1
    # si el limite superior es el mismo que el inferior, entonces no hay solución factible
    while lowerBound < upperBound:
        # forma directa para encontrar el índice
        middlePoint = int(lowerBound + ((upperBound - lowerBound) / (array[upperBound] - array[lowerBound])) *
                          (x - array[lowerBound]))

        if x == array[middlePoint]:
            # x ha sido encontrado
            index = middlePoint
            break
        else:
            if x < array[middlePoint]:
                upperBound = middlePoint - 1
            else:
                lowerBound = middlePoint + 1

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

    # numero a buscar
    x = int(input("ingrese el numero a buscar: \n"))

    # llamado de la función
    index = InterpolationSearch(array, x)
    # impresión de la posición del numero en el arreglo
    print("el número esta en la posición ", (index + 1), " del arreglo")
