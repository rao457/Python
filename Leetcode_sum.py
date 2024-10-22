my_list = [1,3,5,6]
length = len(my_list)
target = 7
def two_sum(my_list, length, target):
    for i in range(length):
        for j in range(i+1,length):
            if my_list[i] + my_list[j] == target:
                yield i, j
                
            
print(list(two_sum(my_list, length, target)))
