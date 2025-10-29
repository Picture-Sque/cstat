import matplotlib.pyplot as plt

# directly give the data (no user input)
heights = [150, 155, 160, 162, 165, 170, 172, 175, 180, 182, 185]

plt.hist(heights, bins=5, edgecolor='black')
plt.title('Distribution of Classmate Heights')
plt.xlabel('Height (cm)')
plt.ylabel('Number of Students')
plt.show()
