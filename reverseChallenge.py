def rev_str(string):
    reversed_string = ''
    for i in range(len(string) -1, -1, -1):
        reversed_string += string[i]
        new = reversed_string
    return new
string = 'hello'
print(rev_str(string))