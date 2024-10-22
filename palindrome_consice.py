""" This programme checks whether the given string reads same forward and backward direction"""
def is_palindrome(my_st):
    my_st = ''.join(char.lower() for char in my_st if char.isalnum())
    return my_st == my_st[::-1]

my_st = 'radar'
print(is_palindrome(my_st))