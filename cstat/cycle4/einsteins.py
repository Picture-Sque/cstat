import numpy as np

def get_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Enter the matrix row by row (space-separated values):")
    matrix = []
    for i in range(rows):
        row = list(map(int,input(f"Row {i+1}: ").split()))

        if len(row) != cols:
            print(f"Error: Row {i+1} must have {cols} columns.")
        matrix.append(row)
    return np.array(matrix)

a= get_matrix()
b=get_matrix()
expr=input("Enter the summation expression: ")
result = np.einsum(expr,a,b)

print("Result:\n",result)