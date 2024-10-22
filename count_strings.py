""" This programme counts the occurence of the letter in the 
string and give us the number"""
my_dict = {}
sting_1 = 'aanekd'
for letter in sting_1.lower():
    if sting_1.count(letter) > 1:
        my_dict[letter] = sting_1.count(letter)
for value in my_dict.values():
    print(value)

        