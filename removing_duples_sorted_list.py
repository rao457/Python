arr = [1, 1, 2, 3,4,4,5,6,6]
my_dict = {}
i = 0
while i < len(arr):
    if arr[i] in my_dict:
        arr.pop(i)
    else:
        my_dict[arr[i]] = i
        i += 1
print(len(arr))