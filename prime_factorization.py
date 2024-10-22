def is_prime(n):
    if n <= 1:
        return False
    elif n <=3:
        return True
    elif n % 2 == 0 and n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 and n % (i+1) == 0:
            return False
n = 4
is_prime(n)