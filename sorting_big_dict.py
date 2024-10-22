def find_second_large(my_list):
    """ This function simply finds the second smallest item in the list"""
    if len(my_list) < 2:
        return None
    my_list.sort()
    return my_list[1]
my_list = [4, 4, 1, 3]
print(find_second_large(my_list))