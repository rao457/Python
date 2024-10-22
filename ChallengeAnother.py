def find_duplicates(original):
    """ This function takes your original list and find duplicates in it and 
    put them into another modified list and return modified list"""
    modified = []
    for i in original:
        if (original.count(i) > 1):
            modified.append(i)
    modified = set(modified)
    return sorted(modified)
prompt =[1, 2, 3, 2, 4, 5, 6, 4, 7, 8, 8, 9]
new = prompt[:]
result = find_duplicates(new)
print(result)
print(prompt)