my_str = 'Hello World'
new_str = ''
for char in my_str:
    new_char = ord(char) + 3
    old_char = chr(new_char)
    new_str += old_char
print(new_str)
o_str = ''
for char in new_str:
    n_char = ord(char) - 3
    o_char = chr(n_char)
    o_str += o_char
print(o_str)

