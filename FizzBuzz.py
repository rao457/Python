# The programme prints from 1 to 100 and multiplies of 3 are indicated by Fizz and 
# multiplies of 5 are indicated by Buzz and multiplies of both are indicated by FizzBuzz
for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    
    