def Conquer(array, lower, mid , higher):
    merged = []
    idx1 = lower
    idx2 = mid+1
    index = 0
    while(idx1 <= mid and idx2 <= higher):
        if (array[idx1]<=array[idx2]):
            merged.append(array[idx1])
            idx1+=1
        else:
            merged.append(array[idx2])
            
            idx2 += 1
    while(idx1 <= mid):
        merged.append(array[idx1])
        
        idx1 += 1
    while(idx2 <= higher):
        merged.append(array[idx2])
    
        idx2 += 1
    # Copying elements from merged to original list
    for i in range(len(merged)):
        array[lower+i] = merged[i]
    
    
    
    
def Divide(array, lower, higher):
    if lower <higher:

        mid = lower + (higher-lower)//2
        Divide(array, lower, mid)
        Divide(array, mid+1, higher)
        Conquer(array, lower, mid, higher)
def main():
    array = [23, 5, 19, 8, 12, 7, 31, 2, 45, 10]
    n = len(array)
    Divide(array, 0, n-1)
    print(array)
if __name__ ==  "__main__":
    main()    

    
