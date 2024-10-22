def reverse_string(input1_str):
    list_2 = input1_str.split()
    new_lst = []
    for word in list_2:
        for i in word:
            new_lst.append(i)
    new_lst.reverse()
    
    reversed_string = ''.join(new_lst)
    print(reversed_string)
input1_str = input("Enter something: ")
reverse_string(input1_str)