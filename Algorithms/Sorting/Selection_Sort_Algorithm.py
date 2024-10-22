def Selection_Sort(my_list):
    """ This programme sort the list by selecting the smallest item and bringing it to its right index in the list"""
    n = len(my_list)
    # It keep track of firstly min index
    for i in range(n-1):
        min_index = i
        # innerloop make another index to compare with outer loop index to sort the list
        for j in range(i+1, n):
            if my_list[j] < my_list[min_index]:
                min_index = j
        
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list
my_list = [234,4,53,23,53,23,5,12]
result = Selection_Sort(my_list)
print(result)