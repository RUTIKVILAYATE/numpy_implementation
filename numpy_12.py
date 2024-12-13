import numpy as np
arr_1 = np.arange(8).reshape(2,4)
arr_2 = np.arange(8,16).reshape(2,4)

print(arr_1)
print(arr_2)


print(arr_1+arr_2)


arr_3 = np.arange(9).reshape(3,3)
arr_4 = np.arange(3).reshape(1,3)

print(arr_3,arr_4)



print(arr_3+arr_4)






arr_1 = np.arange(8).reshape(2,4)
arr_2 = np.arange(8,16).reshape(2,4)

print(arr_1+arr_2) # if x=m and y=n, operation will take place


# if x=1 and y=n, operation will take place(same dimension)
arr_5 = np.arange(3).reshape(1,3)
arr_6 = np.arange(12).reshape(4,3)
print(arr_5+arr_6) 