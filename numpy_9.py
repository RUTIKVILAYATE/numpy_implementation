# Indexing Using Boolean Array
import numpy as np
arr1 = np.array([51,45,34,47,85,67])
arr2 = np.array([4,5,6,7,8,9])

arr1 = arr1.reshape(2,3)
arr5 = np.arange(6).reshape(2,3)
arr4 = np.arange(6,12).reshape(3,2)


print(arr1)

print([arr1>50])
print(arr1[arr1>50])
print(arr1[(arr1>50) & (arr1%2!=0)])

