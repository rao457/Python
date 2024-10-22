""" This program is checking palindromes. Palindrome is word, phrase or sequence
that reads same in forward and backward direction."""
def Check_Palindrome(Your_input):
    """ Fuctions checks your_input for palindrome if it is return True and if it
    is not return False"""
    Your_input = ''.join(char for char in Your_input if char.isalnum()).lower()
    if Your_input == Your_input[::-1]:
        return True
    
Your_input = "$Radar"
result = Check_Palindrome(Your_input)
print(result)