#find the number of occurences of a sequence in numpy array.

import numpy as np
arr1 = np.array([[2,8,9,4],[9,4,9,4],[4,5,9,7],[2,9,4,3]])
#seq = [9,4]

result = repr(arr1).count("9, 4")
print("Count = ",result)