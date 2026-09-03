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
print("grace marks :",array+5)
print("Mean of array is column wise :",np.mean(array,axis=0))
print("Mean of array is row wise :",np.mean(array,axis=1))
print("Minimum of array is column wise:",np.min(array,axis=0))
print("Minimum of array is row wise :",np.min(array,axis=1))
print("Maximum of array is column wise :",np.max(array,axis=0))
print("Maximum of array is row wise :",np.max(array,axis=1))
print("Standard deviation of array is column wise :",np.std(array,axis=0))
print("Standard deviation of array is row wise :",np.std(array,axis=1))
