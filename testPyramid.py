def testDraw(n):
    i = n
    while (i != 0):
        for j in range(0,i-1):
            print(" ", end="")
        for j in range(i-1, n):
            print("*", end="")
            # print(" ",end="")
        for j in range(i, n):
            print("*",end="")
            # print(" ", end="")
        print()
        i-=1
def main():
    my_num = int(input("Enter the numbe to draw the thing: "))
    testDraw(my_num)
if __name__ == "__main__":
    main()