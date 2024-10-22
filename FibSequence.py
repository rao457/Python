def FibSequence(a, b, n):
    if n==0:
        return
    
    c = a+b
    print(c, end=" | ")
    FibSequence(b, c, n-1)
def main():
    n = int(input("Enter the steps we wanna take our series: "))
    a = 0
    b = 1
    print(a, end=" | ")
    print(b, end=" | ")
    FibSequence(a, b, n-2)
main()