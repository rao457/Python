def candle(arr):
    n = len(arr)
    candles = []
    maximum = max(arr)
    for i in range(n):
        if arr[i] == maximum:
            candles.append(i)
    return len(candles)

