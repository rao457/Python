
import string
def vowels_consonants(my_string):
        vowels = 'AEIOUaeiou'
        consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnprstvwxyz'
        vowels_count = 0
        consonants_count = 0


        for char in my_string:
            if char in vowels:
                vowels_count +=1
            elif char in consonants:
                consonants_count += 1
        return vowels_count,consonants_count
my_str = input("Enter Something: ")
result = vowels_consonants(my_str)
print(result)

        
        
        