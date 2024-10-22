def merge_sort(my_list):
    
    n = len(my_list)
    if n <= 1:
        return my_list
    mid = n // 2
    l_half = my_list[:mid]
    r_half = my_list[mid:]
    left = merge_sort(l_half)
    right = merge_sort(r_half)
    return merged(left, right)
def merged(left_half, right_half):
    i,j = 0,0
    new_list = []
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            new_list.append(left_half[i])
            i +=1
        else:
            new_list.append(right_half[j])
            j+=1
    new_list.extend(left_half[i:])
    new_list.extend(right_half[j:])
    return new_list
my_list = [2,3,51,4,79,33,44,32,32,11,13]
print(merge_sort(my_list))