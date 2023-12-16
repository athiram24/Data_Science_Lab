#Create two NumPy arrays of the same shape and perform element-wise addition, subtraction,
#multiplication, and division operations on them.

import numpy as np

# Create two NumPy arrays of the same shape
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

# Perform element-wise addition
addition_result = array1 + array2

# Perform element-wise subtraction
subtraction_result = array1 - array2

# Perform element-wise multiplication
multiplication_result = array1 * array2

# Perform element-wise division
division_result = array1 / array2

print("Array 1:", array1)
print("Array 2:", array2)
print("Element-wise Addition:", addition_result)
print("Element-wise Subtraction:", subtraction_result)
print("Element-wise Multiplication:", multiplication_result)
print("Element-wise Division:", division_result)
