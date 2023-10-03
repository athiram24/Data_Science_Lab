#program to find the product of matrix
import numpy as np
A = [[1,2,3],[4,5,6]]
B = [[7,9,11],[8,10,12]]
Btrans = np.transpose(B)
result = np.dot(A,Btrans)





print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nTranspose of Matrix B:")
print(Btrans)

print("\nResult of A multiplied by the transpose of B:")
print(result)






   
   



