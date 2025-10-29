import numpy as np
arr=np.arange(27).reshape(3,3,3)
print(arr)
for i in range(arr.shape[0]):
    diag=np.diag(arr[i])
    print("Diagonal of matrix",i,":",diag)