
def quick_sort(my_list):
    if len(my_list)<= 1:
        return my_list
            
    mid = len(my_list)//2
    l_half = my_list[:mid]
    r_half = my_list[mid:]
    left_half = quick_sort(l_half)
    right_half = quick_sort(r_half)
    return merged(left_half, right_half)
def merged(left,right):
    new_list = []
    l_idx, r_idx = 0,0
    while l_idx<len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            new_list.append(left[l_idx])
            l_idx += 1
        else:
            new_list.append(right[r_idx])
            r_idx += 1
    new_list.extend(left[l_idx:])
    new_list.extend(right[r_idx:])
    return new_list
my_list = [27, 94, 63, 18, 55, 72, 39, 84, 12, 47, 61, 33, 78, 25, 96, 42, 59, 16, 37, 81, 52, 29, 73, 88, 14, 68, 91, 36, 77, 22, 65, 49, 86, 31, 74, 99, 45, 67, 21, 83, 58, 34, 79, 11, 92, 48, 69, 26, 97, 43, 62, 17, 53, 38, 85, 71, 28, 75, 93, 46, 64, 19, 56, 82, 32, 89, 51, 76, 23, 66, 41, 98, 44, 30, 87, 13, 54, 39, 24, 91, 57, 12, 43, 32, 72, 83, 19, 65, 94, 28, 56, 49, 82, 67, 14, 48, 36, 75, 97, 29, 53, 88, 27, 61, 45, 78, 23, 62, 74, 38, 89, 17, 52, 42, 76, 99, 33, 87, 64, 16, 57, 46, 81, 21, 58, 73, 34, 69, 44, 79, 18, 63, 92, 37, 71, 22, 66, 41, 84, 98, 31, 68, 47, 86, 26, 91, 54, 11, 77, 93, 39, 24, 12, 43, 32, 72, 83, 19, 65, 94, 28, 56, 49, 82, 67, 14, 48, 36, 75, 97, 29, 53, 88, 27, 61, 45, 78, 23, 62, 74, 38, 89, 17, 52, 42, 76, 99, 33, 87, 64, 16, 57, 46, 81, 21, 58, 73, 34, 69, 44, 79, 18, 63, 92, 37, 71, 22, 66, 41, 84, 98, 31, 68, 47, 86, 26, 91, 54, 11, 77, 93]
result = quick_sort(my_list)
print(result)