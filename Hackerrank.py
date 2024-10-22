def matrixDifference(matrix):
    
    right_sum = 0
    left_sum = 0
    n = len(matrix)
    for i in range(n):
        right_sum += matrix[i][i]
        left_sum += matrix[i][n-i-1]
    return abs(right_sum - left_sum)

matrix = [[1, 2, 4], [4, 6, 6], [12, 8, 10]]
print(matrixDifference(matrix))  # Output should be 0
