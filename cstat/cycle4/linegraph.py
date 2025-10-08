import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([2,3,5,7,11])

plt.plot(x,y,color='b')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")   
plt.show()