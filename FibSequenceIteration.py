def fibsequence(n):
    fib_sequence = [0,1]
    for _ in range(2, n):
        next_value = fib_sequence[-1]+fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]
n = int(input("Enter the steps we wanna take our series: "))
result = fibsequence(n)
print(result)