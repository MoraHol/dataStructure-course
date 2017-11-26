def BinarySearch_Recursive(array,x,lB,uB):
    middlePoint = int((lB + uB) / 2 )##if upper bound is equal than lower bound, there is justone feasible
    if(lB == uB):
        if (x == array[middlePoint]):
            ##element x has been found
            return middlePoint
        else:
            return -1
    else:
        if (x == array[middlePoint]):
            return middlePoint
        else:
            if( x < array[middlePoint]):
                return BinarySearch_Recursive(array,x,lB,middlePoint)
            else:
                return BinarySearch_Recursive(array,x,middlePoint + 1,uB)



class main():
    line = input("ingrese los elementos ordenados y separados por coma: \n")
    matInput = line.split(",")
    array = []

    ## fill of array
    for i in range(0, matInput.__len__()):
        array.append(int(matInput[i]))
    int

    ##number to search
    x = int(input("ingrese el numero a buscar: \n"))

    ##called of the funtion
    index = BinarySearch_Recursive(array, x,0,array.__len__())
    print("el número esta en la posición ", (index + 1), " del arreglo")

