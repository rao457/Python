def reverse_string(my_str):
    """ This method reverses a string """
    reversed_string = ''
    for char in range(len(my_str) -1, -1, -1):
        reversed_string += my_str[char]
    return reversed_string
my_str = input("Enter something: ")

result = reverse_string(my_str)
print(result)