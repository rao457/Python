def is_palindrome():
    take = input("Enter something: ")
    take.rstrip()
    take.lstrip()
    if take[::-1].casefold() == take.casefold():
        print(True)
    else: 
        print(False)
is_palindrome()