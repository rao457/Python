punc = "!@#$%^&*()_+-=[]{}|;:,.<>?~"

def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    s = s.translate(str.maketrans("", "", punc))
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal, Panama"))
