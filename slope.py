def main(n):
    i = 1
    for i in range(n):
        print("*" * i)
    while(n>= 0):
        print("*"*n)
        n -= 1
n = 4
main(n)