def Quicksort(array):
    """
    este método ordena un arreglo de números de mayor a menor con ordenamiento Quicksort
    :param array: aquí se recibe el arreglo desordenado
    :return: el arreglo completamente ordenado
    """
    array1 = []  # guarda el arreglo ordenado
    less_subarray = []
    greater_subarray = []

    if (array == []):
        # el arreglo ya esta ordenado
        return array
    else:
        # tomar el primer elemento como pivote
        pivot = array[0]
        for i in range(1, array.__len__()):
            # llenar los sub-arreglos de menores y mayores
            if (array[i] < pivot):
                less_subarray.append(array[i])
            else:
                greater_subarray.append(array[i])
        # aplicar la recursividad para los menores y mayores y concatenar
        less_subarray = Quicksort(less_subarray)
        greater_subarray = Quicksort(greater_subarray)
        # si los arreglos de menores y mayores no contienen números solo agregar el pivote
        if (less_subarray.__len__() < 1 and greater_subarray.__len__() < 1):
            array1.append(pivot)

        else:
            # si el arreglo de menores no contiene números agregar el pivote y el arreglo de mayores
            if (less_subarray.__len__() < 1):
                array1.append(pivot)
                for i in range(0, greater_subarray.__len__()):
                    array1.append(greater_subarray[i])


            else:
                # si el arreglo de mayores no contiene números agregar el arreglo de menores y el pivote
                if (greater_subarray.__len__() < 1):

                    for i in range(0, less_subarray.__len__()):
                        array1.append(less_subarray[i])
                    array1.append(pivot)



                else:
                    # si los dos contienen números agregar los menores, el pivote y por ultimo el de mayores
                    for i in range(0, less_subarray.__len__()):
                        array1.append(less_subarray[i])
                    array1.append(pivot)
                    for i in range(0, greater_subarray.__len__()):
                        array1.append(greater_subarray[i])

    return array1


class main():
    line = input("ingrese los elementos ordenados y separados por coma: \n")
    matInput = line.split(",")
    array = []

    # llenado del arreglo convirtiendo los números de string a enteros
    for i in range(0, matInput.__len__()):
        array.append(int(matInput[i]))
    # llamado de método para ordenar el arreglo
    array = Quicksort(array)
    print("arreglo ordenado:")
    print(array)
