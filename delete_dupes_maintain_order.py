def del_dup(my_list):
    seen = set()
    for i in my_list:
        if i not in seen:
            yield i
            seen.add(i)
my_list = [2,3,4,53,4,32,2,1,1,6]
func = list(del_dup(my_list))
print(id(func))
