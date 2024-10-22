found = {}
my_list = [1, 2,3,4,51,1,4,5,2,6,]
def duplicate_finder(lst):
 
    
    for word in my_list:
        found[word] = found.get(word, 0) + 1 
    return found
result = duplicate_finder(my_list)
print(result)