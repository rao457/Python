encoded_message = input("Enter a message: ")

def encode(message, shift):
    encoded_message= input('ENter message: ')
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encoded_message += chr(shifted)
        else:
            encoded_message += char
    return encoded_message

def decode(encoded_message, shift):
    return encode(encoded_message, -shift)

# Example usage:
message = encoded_message
shift = 3
encoded = encode(encoded_message, shift)
decoded = decode(encoded, shift)

print("Original message:", message)
print("Encoded message:", encoded)
print("Decoded message:", decoded)
