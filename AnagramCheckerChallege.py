# This programe checks whether given inputs are anagrams or not
def Check_Anagrams(str1, str2):
    """ Function is gonna check str1 and str2 for angramy."""
    str1_list = []
    str2_list = []
    # splitting strings for better comparison
    for char in str1.lower():
        str1_list.append(char)
    for char in str2.lower():
        str2_list.append(char)
    # sorting to take easy order to compare the lists of our strings
    if (sorted(str1_list) == sorted(str2_list)):
        print("True")
    else:
        print("False")
# Testing on various inputs from user
str1 = input("Enter First Word: ")
str2 = input("Enter second word: ")
Check_Anagrams(str1, str2)

    