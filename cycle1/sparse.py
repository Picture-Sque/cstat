
matrix = [
    [0, 0, 3],
    [4, 0, 0],
    [0, 5, 6]
]

sparse = {}
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] != 0:
            sparse[(i, j)] = matrix[i][j]

print("Matrix:")
for row in matrix:
    print(row)

print("\nSparse representation:", sparse)
