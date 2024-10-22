def grading(arr):
    new_array = []
    for i in range(len(arr)):
        r = arr[i]%5
        if arr[i] > 37:
            if r > 2:
                if r == 3:
                    new_array.append(arr[i]+2)
                elif r == 4:
                    new_array.append(arr[i]+1)
            else:
                new_array.append(arr[i])
        else:
            new_array.append(arr[i])
    return new_array
arr = [44, 23, 64,23]
print(grading(arr))