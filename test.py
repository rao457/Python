def sort_names(my_list):  
    new_list= []
    for i in my_list:
        new_list.append(len(i))

    n = len(new_list)
    for i in range(1, n):
        key = new_list[i]
        j = i-1
        while j>= 0 and key < new_list[j]:
            new_list[j+1] = new_list[j]
            j -= 1
        new_list[j+1] = key
    sorted_list = []
    my_dict = {}
    for i in new_list:
        value = i
        for name in my_list:
            if len(name) == value:
                my_dict[value] = name
    for value in my_dict.values():
        sorted_list.append(value)
    return sorted_list
arr = ["Apple", "banana", "Orange", "grape", "Pineapple"]
result = sort_names(arr)
print(result)
