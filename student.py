import numpy as np
#Sample Array
array = np.array([[85,90,78],
                  [70,65,80],
                  [95,88,92],
                  [60,75,70],
                  [82,79,85]])


#Basic Operations
print("Original Array:", array)
print("Shape of the Array:", array.shape)
print("Dimensions of array : ", array.ndim)
print("Size of array : ", array.size)
print("Data type of array : ", array.dtype)
print("First student is :",array[0])
print("maths score is :",array[:,0])
print("thirds student score is:",array[2:3,0:3])
print("grace marks :",array+5)


#Statistical Operations
print("Mean of array is column wise :",np.mean(array,axis=0))
result=np.mean(array,axis=1)
print("Mean of array is row wise :",result)
print("Minimum of array is column wise:",np.min(array,axis=0))
print("Minimum of array is row wise :",np.min(array,axis=1))
print("Maximum of array is column wise :",np.max(array,axis=0))
print("Maximum of array is row wise :",np.max(array,axis=1))
print("Standard deviation of array is column wise :",np.std(array,axis=0))
print("Standard deviation of array is row wise :",np.std(array,axis=1))
ans=array[result > 60]
print(ans)


#Reshaping and Flattening
data = np.arange(12)
reshaped = data.reshape(3, 4)
print(reshaped)
flattened = reshaped.flatten()
print(flattened)
array1d=np.arange(5)
print("1D array:",array1d)

#vstack and hstack
new_marks=np.array([[95,85,75]])
update_marks=np.vstack((array,new_marks))
print("Updated marks:",update_marks)
new_marks_col=np.array([[90],[55],[85],[12],[65]])
update_col_marks=np.hstack((array,new_marks_col))
print("Updated marks:",update_col_marks)
array1 = np.array([
    [85, 90],
    [70, 65],
    [95, 88]
])
array2 = np.array([
    [78],
    [80],
    [92]
])
result = np.concatenate((array1, array2), axis=1)
print("concatenated array is : ", result)


#Random Array
random_students = np.random.randint(
    40,
    101,
    size=(2, 3)
)
print("Random array is :",random_students)