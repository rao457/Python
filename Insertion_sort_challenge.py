""" This programme sorts the list of strings on the basis of length of each string puttin smallest on the first and continue in the same order using the insertion sort algorithm."""
def insertion_sort(my_list):
    n = len(my_list)
    for i in range(1, n):
        key = len(my_list[i])
        j = i -1
        while j>=0 and key > len(my_list[j]):
            len(my_list[j+1]) = len(my_list[j])
        