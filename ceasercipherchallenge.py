# This program takes an input file and encrypts it and print the ecrypte file 
# to output file 
def encryption(my_input_file, output_file, shift):
    """ This function takes an input file and encrypts it"""
    encrypted_mate = ''
    try:
        with open(my_input_file, encoding= 'utf-8') as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print(f"File {my_input_file} does not exist.")
    else:
        for char in content:
            if char.isalpha():
                encrypted_chars = ord(char) + shift
                
                if char.isupper():
                    if encrypted_chars > ord('z'):
                        encrypted_chars -= 26
                elif char.islower():
                    if encrypted_chars > ord('Z'):
                        encrypted_chars -= 26
                To_Cat = chr(encrypted_chars)

            else:
                encrypted_chars = char
            encrypted_mate += To_Cat
        # Writing to a new file
        with open(output_file, 'w') as f:
            f.write(encrypted_mate)

def decryption(input_file,output_file, shift):
    """ This function decrypts the encrypted file using special decryption key"""
    decrypted_mate = ''
    try:
        with open(output_file, encoding= 'utf-8') as file:
            my_content = file.read()
    except FileNotFoundError:
        print(f"File {output_file} does not exist.")
    else:
        for char in my_content:
            if char.isalpha():
                decrypted_chars = ord(char) - shift
                if char.islower() < ord('a'):
                    decrypted_chars += 26
                elif char.isupper() < ord('A'):
                    decrypted_chars += 26
                decrypted_to_cat = chr(decrypted_chars)
            else:
                decrypted_chars = char
            decrypted_mate += decrypted_to_cat
        with open(input_file, encoding= 'utf-8') as f:
            content = f.read()
        if content == decrypted_mate:
            print("Your file is successfully decrypted.")
        else:
            print("Some error occured while processing.")

def main():
    """ This function takes user input and holds control over the program."""
    my_input_file = input("Enter Your file name to encrypt: ")
    output_file = input("Enter the file name write encrypted data: ")
    Secret_key = int(input("Enter you secret key: "))
    encryption(my_input_file, output_file, Secret_key)
    print(f"Your file is encrypted and saved as {output_file} successfully.")
    ask_user = input("Do you want to decrypt the file (yes/no): ")
    if ask_user != 'no':

        which_file = input("Enter the name of file to decrypt: ")
        origin_file = input("Enter the name of original file(for security purposes): ")
        Shift_key = int(input("Enter secret Key: "))
        if Shift_key == Secret_key:
            decryption(origin_file,which_file, Shift_key)
        else:
            print("Incorrect secret key.")
    else:
        quit()
main()