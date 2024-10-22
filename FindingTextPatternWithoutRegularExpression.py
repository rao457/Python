def isPhoneNumber(p_number):
    if len(p_number) != 12:
        return False
    for i in range(0,4):
        if not p_number[i].isdecimal():
            return False
    if p_number[4] != '-':
        return False
    for i in range(5,12):
        if not p_number[i].isdecimal():
            return False
    return True

