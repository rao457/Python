def sumInts(n, sum=0):
    if n<0:
        return sum
    sum += n
    
    return sumInts(n-1, sum)
def main():
    n = 4
    print(sumInts(n, 0))
if __name__ == "__main__":
    main()