def Even_separator(my_list):
    """ This function takes list of numbers as input and separate even numbers from list."""
    # Method
    even_numbers = []
    for number in my_list:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers
# Input List
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = Even_separator(my_list)
print(f"Here is the list of Even numbers: {result}")
