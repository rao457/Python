def printNum(current, n):
    if current > n :
        return
    print(current, end=" ")
    printNum(current+1, n)
def main():
    current = int(input("Enter the number from where we start printing: "))
    n = int(input("Enter the number where to stop printing: "))
    printNum(current, n)
main()