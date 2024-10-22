input_1 = input("Enter something: ")
input_2 = input("Enter something: ")
input_1_clean = ''.join(c for c in input_1 if c.isalnum()).lower()
input_2_clean = ''.join(c for c in input_2 if c.isalnum()).lower()
if sorted(input_1_clean) == sorted(input_2_clean):
    print("true")
else:
    print("false")