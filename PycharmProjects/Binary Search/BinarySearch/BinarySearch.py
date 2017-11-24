def BinarySearch(array, x):
    lowerBound = 0
    upperBound = array.__len__() - 1
    index = -1
    ## if upper bound is less than lower bound, there is not a feasible solution
    while(lowerBound < upperBound):
        middlePoint = (lowerBound + upperBound)
        if (x == array[middlePoint]):
            ## x has been found
            index = middlePoint
            break
        else:
            if(x < array[middlePoint]):
                upperBound = middlePoint - 1
            else:
                lowerBound = middlePoint + 1
    if (lowerBound == upperBound and array[lowerBound] == x ):
        index = lowerBound

    return index

class main():
    line = input("ingrese los elementos separados por coma: \n")
    matInput = line.split(",")
    array = []
    ## conversion de String a entero
    for i in range(0,matInput.__len__()):
        array[i] = int(matInput[i])
    print(array)