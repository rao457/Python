# This algorithm works by dividing the array into smaller sub
# sublists and then sorting the sublsts and give us sorted
# list.
def merge_sort(my_list):
    """ This function just divides the list into two halves 
    maybe more than two but it's purpose is to divide"""
    if len(my_list)<= 1:
        return my_list
    mid = len(my_list)//2
    r_half = my_list[mid:]
    l_half = my_list[:mid]
    r_half = merge_sort(r_half)
    l_half = merge_sort(l_half)
    return merge(l_half, r_half)
def merge(left,right):
    """ This function sorts and merges the sublists into bigger sorted list"""
    new = []
    i, j = 0, 0
    # If the indexes we specified for the left and right half sublists
    # is smaller than list of both halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            
            new.append(right[j])
    
            j+= 1
    # Remaining elements are simpley added at the end of 
            # new list by extend method
    new.extend(left[i:])
    new.extend(right[j:])
    return new

my_list = [1,4,6,8,3,4,56,3,43,57]
result = merge_sort(my_list)
print(result)