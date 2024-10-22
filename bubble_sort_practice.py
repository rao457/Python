def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        swapped = True
    return my_list
my_list = [3,4,62,8,5,32]
print(bubble_sort(my_list))