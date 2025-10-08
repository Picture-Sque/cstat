import numpy as np

x=np.array(list(map(int,input("Enter numbers separated by spaces: ").split())))
y=np.array(list(map(int,input("Enter numbers separated by spaces: ").split())))

if len(x)!=len(y):
    print("Error: Arrays must be of the same length.")

corrmatrix=np.corrcoef(x,y)
print("Correlation matrix:\n",corrmatrix)
print("pearson correlation coefficient:",corrmatrix[0,1])