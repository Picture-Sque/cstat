import numpy as np

# population data (given directly)
population = [4779736, 710231, 6392017, 2915918, 37253956, 5029196, 3574097, 897934]

# basic calculations
mean = np.mean(population)
median = np.median(population)
variance = np.var(population)

# display results
print("Mean Population     :",mean)
print("Median Population   :",median)
print("Variance Population :",variance)
