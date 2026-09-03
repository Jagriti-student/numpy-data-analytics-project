import numpy as np
print("Maths","Science,","English")
array = np.array([[85,90,78],
                  [70,65,80],
                  [95,88,92],
                  [60,75,70],
                  [82,79,85]])
print("Original Array:", array)
print("Shape of the Array:", array.shape)
print("Dimensions of array : ", array.ndim)
print("Size of array : ", array.size)
print("Data type of array : ", array.dtype)
print("First student is :",array[0])
print("maths score is :",array[:,0])
print("thirds student score is:",array[2:3,0:3])