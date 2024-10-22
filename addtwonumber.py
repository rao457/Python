def addTwo(n1, n2):
    n1 = str(n1)
    n2 = str(n2)
    n1 = n1[::-1]
    n2 = n2[::-1]
    n1 = int(n1)
    n2 = int(n2)
    n3 = n1 + n2
    n3 = str(n3)
    n3 = n3[::-1]
    return int(n3)
n1 = 243
n2 = 564
result = addTwo(n1, n2)
print(result)