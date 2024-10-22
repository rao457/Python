import string
punc = string.punctuation
def check():
    passwd = input("Enter Your Password: ")
    if 8 > len(passwd) >0 and passwd.isdigit() and passwd.isalnum() and punc in passwd:
        print("Weak! Length must be greater than 8")
    if 8 <= len(passwd) <=16 and passwd.isalnum() :
        print("Moderate! You can make it strong")
    if 16 < len(passwd) <= 24 and punc in passwd and passwd.isalnum:
        print("Strong! Good Password.")
check() 
        
