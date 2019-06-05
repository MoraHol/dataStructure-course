def BinarySearch_Recursive(array, x, lB, uB):
    """

    :param array: el arreglo donde se busca el número
    :param x: el que se va a buscar
    :param lB: índice en el que arranca BinarySearch
    :param uB: índice donde termina BinarySearch
    :return: el índice en el que esta el numero buscado
    """
    middlePoint = int((lB + uB) / 2)
    'si el limite superior es el mismo que el inferior, entonces no hay solución factible'
    if lB == uB:
        if x == array[middlePoint]:
            # el elemento x ha sido encontrado
            return middlePoint
        else:
            return -1
    else:
        if x == array[middlePoint]:
            return middlePoint
        else:
            if x < array[middlePoint]:
                return BinarySearch_Recursive(array, x, lB, middlePoint)
            else:
                return BinarySearch_Recursive(array, x, middlePoint + 1, uB)


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
    index = BinarySearch_Recursive(array, x, 0, array.__len__())
    print("el número esta en la posición ", (index + 1), " del arreglo")
