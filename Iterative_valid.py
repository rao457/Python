def check_valid(str):
    n = len(str)
    for i in range(n):
        if (str[i]=="(" and str[n-i-1]==")"):
            return True
        if (str[i]=="{" and str[n-i-1]=="}"):
            return True
        if (str[i]=="[" and str[n-i-1]=="]"):
            return True
        else:
            return False
str = "{([]]}"
print(check_valid(str))