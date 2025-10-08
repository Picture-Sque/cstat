import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[0,5],[6,7]])
kron = np.kron(a,b)

print("Kronecker product:\n",kron)