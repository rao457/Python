import time
def Count_Down(n):
    i = n
    while (i != 0):
        print(f"{i} \r",end="")
        time.sleep(1)
        i -= 1
n = 20
Count_Down(10)