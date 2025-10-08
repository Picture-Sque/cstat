import numpy as np

matrix = [[1,2,3],[4,5,6],[7,8,9]]

lst=[]

for row in matrix:
    for element in row:
        lst.append(element)

print(lst)