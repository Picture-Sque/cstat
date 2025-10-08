import numpy as np
from math import sqrt

def fibonacci_binet(n):
    sqt = sqrt(5)
    phi=(1+sqt)/2
    psi=(1-sqt)/2

    return int((phi**n-psi**n)/sqt)
n=10
seq=[]
for i in range(n):
    seq.append(fibonacci_binet(i))
print(seq)