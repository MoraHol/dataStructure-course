def Quicksort(array):
    array1 = []
    less_subarray = []
    greater_subarray = []

    if (array == []):
        ## array is already sorted
        return array
    else:
        ## take first set element as a pivot
        pivot = array[0]
        for i in range(1, array.__len__()):
            ## build both less and greater than pivot sub-arrays
            if (array[i] < pivot):
                less_subarray.append(array[i])
            else:
                greater_subarray.append(array[i])
        # call recursion for each one of the subarrays, and concatenate the results
        less_subarray = Quicksort(less_subarray)
        greater_subarray = Quicksort(greater_subarray)
        
        if (less_subarray.__len__() < 1 and greater_subarray.__len__() < 1):
            array1.append(pivot)

        else:
            if (less_subarray.__len__() < 1):
                array1.append(pivot)
                for i in range(0, greater_subarray.__len__()):
                    array1.append(greater_subarray[i])


            else:
                if (greater_subarray.__len__() < 1):

                    for i in range(0, less_subarray.__len__()):
                        array1.append(less_subarray[i])
                    array1.append(pivot)



                else:
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

    ## fill of array
    for i in range(0, matInput.__len__()):
        array.append(int(matInput[i]))

    array = Quicksort(array)
    print("arreglo ordenado:")
    print(array)

