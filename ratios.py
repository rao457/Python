def ratio(arr):
    n = len(arr)
    neg = []
    pos = []
    zeros = []
    for i in range(n):
        if arr[i] < 0:
            neg.append(i)
        elif arr[i] > 0:
            pos.append(i)
        elif arr[i] == 0:
            zeros.append(i)
    negs = len(neg)/n
    poses = len(pos)/n

    zeroses = len(zeros)/n
    print(f"{poses:.6f}")
    print(f"{negs:.6f}")
    print(f"{zeroses:.6f}")
arr = [-4, 3, -9, 0, 4, 1]
ratio(arr)