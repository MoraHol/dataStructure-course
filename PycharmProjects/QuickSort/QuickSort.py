def Quicksort(array):
    j = 0
    less_subarray = []
    greater_subarray = []
    if(array[j] > array[j + 1]):
        ## array is already sorted
        return array
    else:
        ## take first set element as a pivot
        pivot = array[0]
        for i in range(1,array.__len__()):
            ## build both less and greater than pivot sub-arrays
            if(array[i] < pivot):
                less_subarray.append(array[i])
            else:
                greater_subarray.append(array[i])
        ## call recursion for each one of the subarrays, and concatenate the results
        return Quicksort(less_subarray) + pivot + Quicksort(greater_subarray)
class main():
    array = {1,2,3,4}
    for i in range(0,array.__len__()):
        print(array[i])