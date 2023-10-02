#find k smallest elements in an array
import numpy as  np
List = input("Enter the elements space separated")
List1 = List.split()
arr1 = np.array(List1)
print("Array is:",arr1)
#sort() is used to sort
arr = np.sort(arr1)
k = int(input("Enter a number"))
print(arr[:k])





