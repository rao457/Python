""" This programme sorts the list of integers in ascending order"""
def Bubble_Sort(my_array):
    n = len(my_array)
    swapped = False
    for i in range(n):
       

        for j in range(0, n-i-1):
            if my_array[j]>my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
                swapped = True
        if not swapped:
            break
    return my_array
my_array = [3,5,2,8,7]
result = Bubble_Sort(my_array)
print(result)