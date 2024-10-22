# Reverse Method
def reverse(str):
    return str[::-1]
#Input
Give = input("Enter Something: ")
result = reverse(Give)
#print
print(result)
# Palindrome
# Method to Check
def Palindrome(st):
    #Def
    """ If a string reads same in forward and reverse direction is called Palindrome"""
    if st == st[::-1]:
        return True
    else:
        return False
#Input
st = input("Enter Something: ")
result = Palindrome(st) 
print(result)
