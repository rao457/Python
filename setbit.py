def SetBit(n):
    pos = 2
    bitmask = 1<<pos
    new_number = n | bitmask
    return new_number
result = SetBit(8)
print(result)