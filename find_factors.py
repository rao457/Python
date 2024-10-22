
def find_all_factors(num):
    # write your code 
    new_list = []
    for i in range(1,num+1):
        if num% i == 0:
            new_list.append(i)
    return new_list
    

# take user input
num = int(input("Enter a number: "))

# call the function
print(find_all_factors(num))