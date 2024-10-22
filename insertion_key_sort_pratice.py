def insertion_key(my_list):
    n = len(my_list)
    for i in range(1,n):
        key = my_list[i]
        j = i-1
        while j>=0 and key< my_list[j]:
            my_list[j+1] = my_list[j]
            j -=1
        my_list[j+1] = key
    return my_list
my_list = [24,5,7,43,7,45,2,1,5,7]
print(insertion_key(my_list))