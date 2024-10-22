def Place_Tiles(n, m):
    if n==m:
        return 2
    if n<m:
        return 1
    horizontal = Place_Tiles(n-1, m)
    vertical = Place_Tiles(n-m,m)
    total = horizontal + vertical
    return total
n = int(input("Enter the lenght of the floor: "))
m = int(input("Enter the width of the floor: "))
answer = Place_Tiles(n, m)
print(answer)