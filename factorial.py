n = int(input("enter a number: "))
def factorial(n):
    for i in n:
        fact = (n*i)-1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n== -n:
        return None
    else:
        return fact
    
result = factorial(n)
print(factorial)