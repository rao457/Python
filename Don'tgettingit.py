# 1
def Bubble_Sort(my_list):
    n = len(my_list)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if my_list[j]> my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
            swapped = True
    return my_list
my_list = [3,6,2,8,5]
print(Bubble_Sort(my_list))
# 2
def selection_sort(my_list):
    n = len(my_list)
    for i in range(n-1):
        min_index = i
        
        for j in range(i+1, n):
            if my_list[min_index] > my_list[j]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list
my_list = [3,6,2,8,5]
print(selection_sort(my_list))
# 3
def insertion_key(my_list):
    n = len(my_list)
    for i in range(1,n):
        key = my_list[i]
        j = i - 1
        while j >= 0 and key < my_list[j]:
            my_list[j+1] = my_list[j]
            j -= 1
            my_list[j+1] = key
    return my_list
my_list = [3,6,2,8,5]
print(insertion_key(my_list))
# 4
def quick_sort(my_list):
    if len(my_list)<= 1:
        return my_list
    else:
        mid = my_list[0]
        lesser = [x for x in my_list[1:] if x <= mid]
        greater = [x for x in my_list[1:] if x > mid]
    return quick_sort(lesser) + [mid] + quick_sort(greater)
my_list = [3,6,2,8,5]
print(quick_sort(my_list))
# 5
def merge_sort(my_list):
    if len(my_list)<= 1:
        return my_list
    mid = len(my_list)//2
    l_half = my_list[:mid]
    r_half = my_list[mid:]
    left = merge_sort(l_half)
    right = merge_sort(r_half)
    return merged(left,right)
def merged(left_h, right_h):
    new_list = []
    i, j = 0,0
    while i<len(left_h) and j<len(right_h):
        if left_h[i]<right_h[j]:
            new_list.append(left_h[i])
            i += 1
        else:
            new_list.append(right_h[j])
            j += 1
    new_list.extend(left_h[i:])
    new_list.extend(right_h[j:])
    return new_list
my_list = [3,6,2,8,5]
print(merge_sort(my_list))