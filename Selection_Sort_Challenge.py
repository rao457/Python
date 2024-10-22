""" This programme finds the smallest item specified by the user in the given list on integers"""
def Selection_Sort(my_array, k):
    n = len(my_array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if my_array[j]<my_array[min_index]:
                min_index = j
                
        my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
    return my_array[k-1]
def input_validation(my_array):
    k = 0
    k_th_element = input("Enter smallest element to find: ")
    
    if k_th_element.isdigit():    
        k_th_element = int(k_th_element)
        if 1<= k_th_element <= len(my_array):
            k =  k_th_element
        else:
            print('Value out of bound')
            quit()
    else:
        print('please provide valid integer')
        quit()

    selection_func = Selection_Sort(my_array, k)
    return selection_func
my_array = [29, 14, 56, 3, 78, 42, 9, 17, 62, 5]
result = input_validation(my_array)
print(result)

        
    

    