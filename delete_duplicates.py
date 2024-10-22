def Delete_Dupes(arr, index, newString, seen):
    if index == len(arr):
        
        print(newString)
        return
    curr_Char = arr[index]
    curr_index = ord(curr_Char)- ord('a')
    if seen[curr_index]:
        Delete_Dupes(arr, index+1, newString, seen)
    else:
        newString += curr_Char
        seen[curr_index] = True
        Delete_Dupes(arr, index+1, newString, seen)
arr = "aabbccdd"
seen = [False]*26
Delete_Dupes(arr, 0, "", seen)