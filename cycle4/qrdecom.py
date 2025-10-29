import numpy as np
a= np.array([[1,1],[1,0],[0,1] ])
q,r=np.linalg.qr(a)
print("matrixq:",q)
print("matrixr:",r)

print("\n check if q@r equals a:",np.allclose(a,q@r))