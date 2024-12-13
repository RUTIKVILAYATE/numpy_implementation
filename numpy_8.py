import numpy as np
arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([4,5,6,7,8,9])

arr3 = np.arange(6).reshape(2,3)
arr5 = np.arange(6).reshape(2,3)
arr4 = np.arange(6,12).reshape(3,2)

print(arr3)
print(arr4)







# ravel()   --> convert multi-D into 1-D 
arr3_1d = arr3.ravel()
print(arr3_1d)


# reshape() --> reshape the array into special dimension based on the correct factors
arr_reshaped = arr3.reshape(2,3)
print(arr_reshaped)




# transpose()   --> transposes the array
arr3_transpose = arr3.transpose()   
print(arr3_transpose)

# stacking() --> combining two arrays    two types
# arr3_4_combine = np.hstack(arr3)
arr3_4_combine = np.vstack(arr3)
print(arr3_4_combine)





arr_split = np.hsplit(arr3,3)
print(arr_split)


arr4_split = np.vsplit(arr4,3)
print(arr4_split)