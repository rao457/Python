# This Method reads a file and containing numbers and gives sum of the numbers
# in the file
def Read_Sum_File(filename):
    """ This function opens file containing number and give us sum of them."""
    try:
        with open(filename, 'r') as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print("Sorry, {filename} file does not exist.")
    else:
        content = content.split(",")
        my_sum = sum(int(num)for num in content)
        return my_sum
# Calling Method
result = Read_Sum_File('Numbers.txt')
print(f"The sum of numbers in the file is {result}.")