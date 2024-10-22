def findPair(array, target, start):
    if (start >= len(array)):
        return False
    return findPairRec(array, target, start, start+1)
def findPairRec(array, target, start, next):
    if (next >= len(array)):
        return findPair(array, target, start+1)
    if (array[start] + array[next] == target):
        print(f"Pair found: {array[start]}, {array[next]}.")
        return True
    return findPairRec(array, target, start, next+1)
def main():
    array = [1,2,3,5,6,4,8]
    target = 13
    result = findPair(array, target, 0)
    if not result:
        print("Pair Not found.")
if __name__ == "__main__":
    main()