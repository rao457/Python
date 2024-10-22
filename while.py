def is_valid(my_st):
    """ This function checks if the string contains the correct arrangement of brackets in it"""
    has_paranthesis = False
    has_square = False
    has_curly = False
    closings = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    stack = []
    for symbol in my_st:
        if symbol in '([{':
            stack.append(symbol)
        elif symbol in closings:
            if not stack or stack[-1] != closings[symbol]:
                return False
            stack.pop()
    return not stack
my_st = "({})"
result = is_valid(my_st)
print(result)