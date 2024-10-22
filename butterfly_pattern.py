def butterfly(n):
    n_ = n + 1
    # Upper half
    for i in range(1, n_):
        # Stars
        for j in range(1, i + 1):
            print("*", end='')
        # Spaces
        for j in range(1, 2 * (n - i) + 2):
            print(" ", end='')
        # Stars
        for j in range(1, i + 1):
            print("*", end='')
        print()
    # Lower half
    for i in range(n, 0, -1):
        # Stars
        for j in range(1, i + 1):
            print("*", end='')
        # Spaces
        for j in range(1, 2 * (n - i) + 2):
            print(" ", end='')
        # Stars
        for j in range(1, i + 1):
            print("*", end='')
        print()

butterfly(5)
