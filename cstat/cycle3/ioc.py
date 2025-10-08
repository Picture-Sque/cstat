import numpy as np

a=np.array([1,2,3])
b=np.array([4,5,6])
inner=np.inner(a,b)
out=np.outer(a,b)
cro=np.cross(a,b)

print("Vector A",a)
print("Vector B",b)
print("Inner Product:",inner)
print("Outer Product:\n",out)
print("Cross Product:",cro)