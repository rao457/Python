def Bubble_Sort(my_list):
    """ This algorithm sorts list ascending order as bubble come up in the water"""
    n = len(my_list)
    # Keep track of index
    for i in range(n):
        swapped = False
        # Innerloop to sort elements correctly
        for j in range(0, n-i-1):
            if my_list[j]> my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                swapped = True
    return my_list
my_list = [23,3,2,32,53,45,33,4]
result = Bubble_Sort(my_list)
print(result)
