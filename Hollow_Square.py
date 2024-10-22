def print_hollow_square(size):
    if size < 2:
        print("Size should be 2 or larger.")
        return

    for i in range(size):
        if i == 0 or i == size - 1:
            print('*' * size)
        else:
            print('*' + ' ' * (size - 2) + '*')

# Example usage:
print_hollow_square(5)
