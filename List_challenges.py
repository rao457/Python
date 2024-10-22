def check_big(ls):
    if not ls:
        return None
    big = ls[0]
    for num in ls:
        if num > big:
            big = num
    return big
my_list= [434,54,62,32,4543,5,65,32]
print(check_big(my_list))