import numpy as np

# np.array() -> Used to create a NumPy array
print("Array is : ", np.array([1, 2, 3, 4, 5]))

# np.zeros() -> Used to create an array filled with zeros
print("Zeroes array is : ", np.zeros([2, 2]))

# np.ones() -> Used to create an array filled with ones
print("Onees array is : ", np.ones([2, 2]))

# np.arange() -> Used to create numbers within a specified range
list = np.arange(1, 9)
print(list)

# np.linspace() -> Used to create equally spaced values
arr = np.linspace(0, 10, 5)
print(arr)

# np.eye() -> Used to create an identity matrix
print("Identity matrix is : ", np.eye(3))

# np.random.rand() -> Used to generate random decimal values between 0 and 1
arr1 = np.random.rand(5)
print(arr1)

arr2 = np.random.rand(3, 4)
print(arr2)

# np.random.randint() -> Used to generate random integers within a range
arr3 = np.random.randint(1, 100, 6)
print(arr3)

arr4 = np.random.randint(1, 100, (2, 2))
print(arr4)

# reshape() -> Used to change the shape of an array
rshape = arr3.reshape(2, 3)
print(rshape)

# flatten() -> Used to convert a multi-dimensional array into 1D
flattened = rshape.flatten()
print(flattened)

# ravel() -> Used to flatten an array into 1D
raveled = flattened.ravel()
print(raveled)

# Broadcasting -> Used to perform operations on all elements at once
list1 = np.array([1, 2, 3, 4, 5, 6])
print(list1 + 5)
print(list1 * 5)
print(list1 ** 5)

list2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(list2)
print(list2 + 5)
print(list2 * 5)
print(list2 ** 2)

# Boolean Indexing -> Used to filter elements based on conditions
print(list2[list2 % 2 == 0])
print(list2[(list2 > 3) & (list2 < 6)])

# np.sort() -> Used to sort array values in ascending order
list3 = np.array([9, 5, 7, 2, 1, 4, 8, 3, 0, 8])
ascending = np.sort(list3)
print("Ascending order of list : ", ascending)

# np.argsort() -> Used to get indexes that would sort the array
asc = np.argsort(list3)
print(asc)

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# np.dot() -> Used to perform matrix multiplication
result = np.dot(A, B)
print(result)

# np.matmul() -> Used to perform matrix multiplication
result1 = np.matmul(A, B)
print(result1)

C = np.array([[1, 2, 3], [4, 5, 6]])

# np.transpose() -> Used to convert rows into columns
print(np.transpose(C))

# np.linalg.det() -> Used to calculate determinant of a square matrix
determinant = np.linalg.det(A)
print(determinant)

# np.linalg.inv() -> Used to calculate inverse of a matrix
inverse = np.linalg.inv(A)
print(inverse)