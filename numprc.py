#in the name of cod 
#numpy textbook 
# firstly we need import

import numpy as np

#then creat a numpy array like list
my_array = np.array([1, 2, 3, 4, 5])
print(my_array)

#review matrix

#now creat arrays without enter numbers manually
#since zero
# creates an array with 5 elements  all of which are zero.
zeros = np.zeros(5)
print(zeros)  #[0. 0. 0. 0. 0.]
ones = np.ones(5) #[1. 1. 1. 1. 1.]


#where is it used? when we want to make array and after change its element


range_array = np.arange(0, 10, 2) #start=0, stop=10, step=2
print(range_array) #[0 2 4 6 8 ]