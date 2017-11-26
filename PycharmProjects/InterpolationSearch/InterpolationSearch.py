def InterpolationSearch (array,x):
    lowerBound = 0
    upperBound = array.__len__() - 1
    index = -1
    ## if upper bound is less bound¿, there is not a feasilbe solution
    while( lowerBound < upperBound):
        middlePoint = lowerBound + ((upperBound - lowerBound) /
                                    (array[upperBound] - array[lowerBound])) * (x - array[lowerBound])

        if ( x == array[middlePoint]):
            ## x has been found
            index = middlePoint
            break
        else:
            if(x < array[middlePoint]):
                upperBound = middlePoint - 1
            else:
                lowerBound = middlePoint + 1

    if(lowerBound == upperBound and array[lowerBound] == x):
        index = lowerBound

    return  index
class main():
    line = input("ingrese los elementos ordenados y separados por coma: \n")
    matInput = line.split(",")
    array = []

    ## fill of array
    for i in range(0, matInput.__len__()):
        array.append(int(matInput[i]))


    ##number to search
    x = int(input("ingrese el numero a buscar: \n"))

    ##called of the funtion
    index = InterpolationSearch(array, x)
    print("el número esta en la posición ", (index + 1), " del arreglo")