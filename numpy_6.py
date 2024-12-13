import numpy as np
arr1 = np.arange(24)
# print(arr1)

arr_reshaped = arr1.reshape(6,4)
print(arr_reshaped)






print("extract all the rows and all the third coloumnth elements")



print(arr_reshaped[:,2])

print("extract all the elements in the second column of the array")
print(arr_reshaped[:,1:3])


# extract 9,10,13,14

print(arr_reshaped[2:4,1:3])

# extract 18,19,22,23

print(arr_reshaped[4:,2:])




for items in arr_reshaped:
    print(items)




for items in np.nditer(arr_reshaped):
    print(items)
