import time
def count_down(n):
    print(f"Count down starts at {n}: ")
    while n>0:

        print(n)

        time.sleep(0.4)
        n -= 1
count_down(23)