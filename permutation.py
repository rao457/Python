

def permutation(string, combination):
    """ It is the permutation code to find all the possible combination of solutions in a given sequence """
    if (len(string) == 0):
        print(combination)
        return
    # For loop to loop over the string and take character one by one
    for i in range(len(string)):
        currChar = string[i]
        # making a new string excluding the current character and making the new string of the remaining characters
        newString = string[0:i] + string[i+1:]
        permutation(newString, combination+currChar)
Test_string = "abc"
permutation(Test_string, "")