original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
modified_list = []
def modify_list():
    
    """ This function would remove all even words from a list and double all
    odd numbers and put them into a new list and return new list"""

    
    for i in original:
        if (i % 2 != 0):
            modified_list.append(i*2)
    return modified_list

result = modify_list()
print(result)