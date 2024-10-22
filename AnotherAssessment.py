def Sum_Evens(my_lst):
    """ This function takes list of number as input and returns sum of all the even number in the list"""
    even_lst = []
    if my_lst:
        for i in my_lst:
            if isinstance(i, int):
                if i % 2 == 0:
                    even_lst.append(i)
            elif not isinstance(i, int):
                my_lst.remove(i)
                
    else:
        print("Please Input a list to start.")            
    my_sum = sum(even_lst)
    return my_sum
my_lst = ['harry',1,2,3,4,5,6,7,8,9,10,12,'shoaib']
Sum_Evens(my_lst)
