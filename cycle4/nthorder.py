import numpy as np

arr = np.array(list(map(int, input("Enter numbers separated by spaces: ").split())))
print("Original array:", arr)
n=int(input("Enter the nth order of difference(n): "))
diff_arr = np.diff(arr, n=n)

print(f"{n}th order difference:", diff_arr)