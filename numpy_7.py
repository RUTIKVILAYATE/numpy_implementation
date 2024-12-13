import numpy as np
arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([4,5,6,7,8,9])

print(arr1-arr2)          # element wise subtraction
print(arr1*arr2)          # element wise multiplication     --> vector is multiplied with another vector --> thus called vector multiplication
print(arr1*2)             # every item is multiplied by 2       in mathematics --> vector is scaled by the scaler value and it will grow --> thus called scaler multiplication




print(arr2>3)            # compared each value with 3
print(arr1>3)            # compared each value with 3



arr3 = np.arange(6).reshape(2,3)
arr4 = np.arange(6,12).reshape(3,2)


print(arr3.dot(arr4))       # dot product of the same shaped matrices

print(arr1.dot(arr2))       # same shaped matrix 

# print(arr1.dot(arr3))       # different shaped matrices doesnt compute 




print(arr4.max())
print(arr4.min())



print(arr4)

print(arr4.max(axis=0))    # column wise maximum 

print(arr4.max(axis=1))    # row wise maximum


print(arr4.sum())           # sum of the all the elements in the vector
print(arr4.sum(axis=0))     # column wise sum
print(arr4.sum(axis=1))     # row wise sum  




print(arr4.mean())            # mean of the matrix value 
print(arr4.mean(axis=0))      # mean of the column value   |  2 columns 2 values
print(arr4.mean(axis=1))      # mean of the row value      |  3 rows three value





# print(arr4.median())     there is no median() in the numpy
# print(arr4.mode())       there is no mode() in the numpy

# instead use --> np.median(), np.mode()

print(np.median(arr4))
# print(np.mod(arr4))



print(arr4.std())            # standard deviation
print(arr4.std(axis=0))            # standard deviation of column
print(arr4.std(axis=1))            # standard deviation of row





print(np.sin(arr4))      # sin value of the matrix values
print(np.sin(arr4) )     # sin value of the matrix values
print(np.sin(arr4))      # sin value of the matrix values



print(np.exp(arr4))