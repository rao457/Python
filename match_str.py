def findSubArray(strings):
    for i in range(len(strings)):
        for j in range(i, len(strings)+1):
            for k in range(i , j):
                print(strings[k],end="")
            print(" ", end="")
        print()
strings = "abcdef"
findSubArray(strings)