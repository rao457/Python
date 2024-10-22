def insertion_sort(my_list):
    n = len(my_list)
    # We iterate from second element actually it is the key which is we gonna compare with the element before it  to sort the list.

    for i in range(1, n):
        # i at any time is the key but we spcifiy the index of j so that it is always before i and we can compare them
        key = my_list[i]
        # j is before i
        j = i-1
        # Inner while loop
        # We set the condition that the index j is greater than or equal to 0 but key(index((i))) is always greate than index j

        while j>=0 and key < my_list[j]:
            # We check if element after j is equal to j
            my_list[j+1] = my_list[j]
            # Then we move j one position back
            j -= 1
            # One element after j is now key  to compare j and sort the list 
            
            my_list[j+1] = key
    return my_list
my_list = [1,4,6,8,3,4,56,3,43,57]
result = insertion_sort(my_list) 
print(result)