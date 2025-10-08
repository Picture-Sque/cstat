import numpy as np

ev,er=np.linalg.eig(np.array([[1,2],[2,1]]))
print("eigen values:",ev)
print("eigen vectors:\n",er)

for i in range(len(ev)):
    av=np.dot(np.array([[1,2],[2,1]]),er[:,i])
    lv=ev[i]*er[:,i]
    print(f"\n check for eigen value {i+1}:")
    print("Av:",av)
    print("λv:",lv)