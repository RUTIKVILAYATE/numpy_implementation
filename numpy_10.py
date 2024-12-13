import numpy as np

# creatin a linear space between -40,40 with 100 values between them 
arr_x = np.linspace(-40,40,100)
print(arr_x)


y_sin = np.sin(arr_x)
print("Y_sin:", y_sin)



print(len(arr_x))
print(y_sin.size)



import matplotlib.pyplot as plt
%matplotlib inline     # used to plot the graph in jupyter notebook


plt.plot(arr_x,y_sin)



y = arr_x*arr_x + 2*arr_x + 6           # parabola graph 
plt.plot(arr_x,y_sin)