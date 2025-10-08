import numpy as np

A=np.array([[1,2],[3,4]])
print("Matrix A : ")
print(A)

A_inv=np.linalg.inv(A)
print("Inverse of A is :\n",A_inv)