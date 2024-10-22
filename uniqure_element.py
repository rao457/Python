# def unique_elements(my_list):
#     unique_list = list(set(my_list))
#     return unique_list
# my_list = [1, 1, 2, 2, 3, 3, 4, 4]
# result = unique_elements(my_list)
# print(result)
def unique_elements(my_array):
    unique_list = []
    seen = set()
    for item in my_array:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list
result = unique_elements([1, 1, 2, 2, 3, 3, 4, 4])
print(result)