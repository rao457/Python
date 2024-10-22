def partition(array, low, high):
    pivot = array[high]
    n = low-1
    for j in range(low, high):
        if array[j] < pivot:
            n+=1
            #swap
            


def quick_java(array, low, high):
    if low < high:
        p_index = partition(array, low, high)
        quick_java(array, low, p_index-1)
        quick_java(array, p_index+1, high)
    