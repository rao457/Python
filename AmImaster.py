""" This program is gonna take list of numbers and would find mean, mode and
median of them"""
def mean(my_nums):
    """ Function is gonna find mean of numbers which is the average of numbers"""
    return sum(my_nums)/2
def mode(my_nums):
    """ Function is gonna find the mode of numbers"""
    my_mode = len(sorted(my_nums))/2
    return my_nums[my_mode]
