import time
def stopwatch(n):
    if n==0:
        return
    print(n, end=' ')
    time.sleep(1)
    stopwatch(n-1)
stopwatch(10)