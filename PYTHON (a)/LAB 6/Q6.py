import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

row = len(arr)
column = len(arr[0])
print("Number of rows: ", row)
print("Number of columns: ", column)
if row == column:
    print("square matrix")
else:
    print("non square matrix / rectangular matrix")

print("Dimensions: ", row, "x", column)
