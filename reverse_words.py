# def words_reverse():
#     file = input("Enter the file name to reverse: ")
#     if file:
#         with open(file, 'r') as f:
#             for line in f.readlines():
#                 line = line.split()
#                 for word in line:
                    
#                     save = word[ : : -1]
#                     save = ''.join(save)
#         with open('newfile', 'w') as f:
#             f.write(save)
#     else: 
#         print("File does not exist.")
# words_reverse()
def reverse_word(word):
    # Reverses a single word
    return word[::-1]

def reverse_words_in_file(input_file, output_file):
    # Open the input file for reading
    with open('My_Text.txt', 'r') as file:
        content = file.read()
    
    # Split the content into words
    words = content.split()

    # Reverse each word
    reversed_words = [reverse_word(word) for word in words]

    # Join the reversed words back into a string
    reversed_content = ' '.join(reversed_words)

    # Open the output file for writing
    with open(output_file, 'w') as file:
        # Write the reversed content into the new file
        file.write(reversed_content)

# Example usage:
input_file = 'input.txt'
output_file = 'output.txt'
reverse_words_in_file(input_file, output_file)
print("Words reversed and stored in", output_file)
