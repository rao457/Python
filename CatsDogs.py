# This programm reads the contents of two files cats.txt and dogs.txt and print
# the content to screen
def Read_File(first_file):
    """ This function reads two files simultaneously and print the content"""
    try:
        with open(first_file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Your file {first_file} does not exist.")
    else:
        return content
result = Read_File('cats.txt')
print(result)
