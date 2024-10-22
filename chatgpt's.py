import hashlib

def encrypt_char(char, shift):
    """Encrypts a single character."""
    if char.isalpha():
        encrypted_char = ord(char) + shift
        if char.islower():
            if encrypted_char > ord('z'):
                encrypted_char -= 26
        elif char.isupper():
            if encrypted_char > ord('Z'):
                encrypted_char -= 26
        return chr(encrypted_char)
    return char

def decrypt_char(char, shift):
    """Decrypts a single character."""
    if char.isalpha():
        decrypted_char = ord(char) - shift
        if char.islower():
            if decrypted_char < ord('a'):
                decrypted_char += 26
        elif char.isupper():
            if decrypted_char < ord('A'):
                decrypted_char += 26
        return chr(decrypted_char)
    return char

def encryption(input_file, output_file, shift):
    """Encrypts the input file."""
    try:
        with open(input_file, 'r', encoding='utf-8') as file_in:
            content = file_in.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    encrypted_content = ''.join(encrypt_char(char, shift) for char in content)

    with open(output_file, 'w', encoding='utf-8') as file_out:
        file_out.write(encrypted_content)
    print(f"Encryption complete. Encrypted file saved as '{output_file}'.")

def decryption(input_file, output_file, shift):
    """Decrypts the input file."""
    try:
        with open(input_file, 'r', encoding='utf-8') as file_in:
            encrypted_content = file_in.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    decrypted_content = ''.join(decrypt_char(char, shift) for char in encrypted_content)

    with open(output_file, 'w', encoding='utf-8') as file_out:
        file_out.write(decrypted_content)
    print(f"Decryption complete. Decrypted file saved as '{output_file}'.")

def compare_files(file1, file2):
    """Compares two files by calculating their MD5 hash."""
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        hash1 = hashlib.md5(f1.read()).hexdigest()
        hash2 = hashlib.md5(f2.read()).hexdigest()
    return hash1 == hash2

def main():
    """Main function to control program flow."""
    input_file = input("Enter the name of the file to encrypt: ")
    output_file = input("Enter the name of the encrypted file: ")
    shift = int(input("Enter the encryption shift value: "))

    encryption(input_file, output_file, shift)

    decrypt = input("Do you want to decrypt the file? (yes/no): ")
    if decrypt.lower() == 'yes':
        decrypted_file = input("Enter the name of the decrypted file: ")
        decryption(output_file, decrypted_file, shift)

        if compare_files(input_file, decrypted_file):
            print("Decryption successful. The decrypted file matches the original file.")
        else:
            print("Decryption failed. The decrypted file does not match the original file.")

if __name__ == "__main__":
    main()
