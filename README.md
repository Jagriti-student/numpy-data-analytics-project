# 📊 NumPy Data Analytics Project

A comprehensive hands-on repository documenting my journey of learning **NumPy from basic to advanced concepts** through practical examples, array operations, data analysis, and mini projects.

This repository focuses on understanding how NumPy can be used for efficient numerical computation, multidimensional array manipulation, statistical analysis, boolean indexing, broadcasting, sorting, and matrix operations.

---

## 🚀 About NumPy

**NumPy (Numerical Python)** is a powerful Python library used for numerical computing and data analysis.

It provides:

- Fast and efficient multidimensional arrays
- Mathematical and statistical operations
- Array manipulation
- Matrix operations
- Broadcasting
- Boolean indexing
- Random data generation
- Linear algebra operations

One of the biggest advantages of NumPy is that it allows us to perform operations on entire arrays without writing traditional loops.

---

# 📚 Concepts Practiced

## 1️⃣ Array Creation

Learned different ways to create NumPy arrays.

| Function | Description |
|----------|-------------|
| `np.array()` | Create a NumPy array manually |
| `np.zeros()` | Create an array filled with zeros |
| `np.ones()` | Create an array filled with ones |
| `np.arange()` | Create values within a specified range |
| `np.linspace()` | Create equally spaced values |
| `np.eye()` | Create an identity matrix |

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
zeros = np.zeros((2, 2))
ones = np.ones((3, 3))
numbers = np.arange(1, 10)
```

---

## 2️⃣ Random Array Generation

Practiced generating random arrays for testing and experimentation.

| Function | Description |
|----------|-------------|
| `np.random.rand()` | Generate random decimal values between 0 and 1 |
| `np.random.randint()` | Generate random integers within a range |

Example:

```python
random_values = np.random.rand(5)
random_matrix = np.random.rand(3, 4)
random_integers = np.random.randint(1, 100, 10)
```

---

## 3️⃣ Array Properties

Learned how to inspect NumPy arrays.

| Property | Description |
|----------|-------------|
| `.shape` | Returns dimensions of an array |
| `.ndim` | Returns number of dimensions |
| `.size` | Returns total number of elements |
| `.dtype` | Returns data type of elements |

Example:

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
```

---

## 4️⃣ Indexing and Slicing

Practiced accessing individual elements and extracting portions of arrays.

### Concepts Practiced

- Single element indexing
- Negative indexing
- Array slicing
- 2D array indexing
- Row selection
- Column selection
- Sub-array extraction

Example:

```python
arr[0]
arr[-1]
arr[1:5]

matrix[0, 1]
matrix[:, 0]
matrix[0, :]
```

---

## 5️⃣ Reshaping Arrays

Learned how to change the structure of NumPy arrays.

| Function | Description |
|----------|-------------|
| `reshape()` | Change the shape of an array |
| `flatten()` | Convert a multidimensional array into 1D |
| `ravel()` | Flatten an array into 1D |

Example:

```python
arr = np.arange(1, 7)

reshaped = arr.reshape(2, 3)
flattened = reshaped.flatten()
raveled = reshaped.ravel()
```

### Concept Flow

```text
1D Array
   ↓
reshape()
   ↓
2D Array
   ↓
flatten() / ravel()
   ↓
1D Array
```

---

## 6️⃣ Mathematical Operations

Performed mathematical operations directly on NumPy arrays.

### Operations Practiced

- Addition
- Subtraction
- Multiplication
- Division
- Power

Example:

```python
arr = np.array([1, 2, 3, 4])

print(arr + 5)
print(arr * 2)
print(arr ** 2)
```

NumPy performs these operations on all elements efficiently.

---

## 7️⃣ Broadcasting

Broadcasting allows NumPy to perform operations on entire arrays without manually writing loops.

Example:

```python
arr = np.array([1, 2, 3, 4])

print(arr + 10)
print(arr * 5)
print(arr ** 2)
```

Instead of using loops for every element, NumPy allows vectorized operations such as:

```python
arr * 5
```

This makes numerical computation faster and cleaner.

---

## 8️⃣ Boolean Indexing

Used conditions to filter specific elements from NumPy arrays.

### Examples Practiced

```python
arr[arr > 10]
arr[arr % 2 == 0]
arr[(arr > 3) & (arr < 10)]
```

### Applications

- Find even numbers
- Find odd numbers
- Filter values greater than a specific value
- Filter values below a specific value
- Apply multiple conditions
- Modify array values based on conditions

---

## 9️⃣ Array Modification

Practiced modifying elements in arrays based on specific conditions.

Examples include:

- Replacing values above a certain limit
- Modifying selected values
- Updating numerical data
- Applying conditions to arrays

Example:

```python
arr[arr > 100] = 100
```

This allows efficient modification of multiple values without loops.

---

## 🔟 Statistical Operations

Used NumPy functions to analyze numerical data.

| Function | Description |
|----------|-------------|
| `np.sum()` | Calculate total |
| `np.mean()` | Calculate average |
| `np.median()` | Find middle value |
| `np.min()` | Find minimum value |
| `np.max()` | Find maximum value |
| `np.std()` | Calculate standard deviation |
| `np.var()` | Calculate variance |
| `np.argmax()` | Find index of maximum value |
| `np.argmin()` | Find index of minimum value |

Example:

```python
arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.argmax(arr))
```

---

## 1️⃣1️⃣ Axis Operations

Learned how operations behave across rows and columns in multidimensional arrays.

For a 2D array:

```text
axis = 0 → Column-wise operation
axis = 1 → Row-wise operation
```

Example:

```python
matrix.sum(axis=0)
matrix.sum(axis=1)

np.mean(matrix, axis=0)
np.mean(matrix, axis=1)
```

The `axis` concept is important for multidimensional data analysis.

---

## 1️⃣2️⃣ Sorting

Practiced sorting NumPy arrays.

| Function | Description |
|----------|-------------|
| `np.sort()` | Sort array values |
| `np.argsort()` | Return indexes that would sort the array |

Example:

```python
arr = np.array([9, 5, 7, 2, 1])

print(np.sort(arr))
print(np.argsort(arr))
```

### Difference

```text
np.sort()
↓
Returns sorted values

np.argsort()
↓
Returns indexes that would sort the array
```

---

## 1️⃣3️⃣ Matrix Operations

Practiced fundamental matrix operations using NumPy.

### Operations Covered

- Matrix addition
- Matrix subtraction
- Element-wise multiplication
- Matrix multiplication
- Matrix transpose
- Determinant
- Matrix inverse

### Element-wise Multiplication

```python
A * B
```

Multiplies corresponding elements of two arrays.

### Matrix Multiplication

#### `np.dot()`

Used to perform dot product and matrix multiplication.

```python
result = np.dot(A, B)
```

#### `np.matmul()`

Used to perform matrix multiplication.

```python
result = np.matmul(A, B)
```

---

## 1️⃣4️⃣ Matrix Transpose

### `np.transpose()`

Used to convert rows into columns and columns into rows.

Example:

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.transpose(A))
```

Output:

```text
[[1 4]
 [2 5]
 [3 6]]
```

---

## 1️⃣5️⃣ Determinant

### `np.linalg.det()`

Used to calculate the determinant of a square matrix.

Example:

```python
A = np.array([
    [1, 2],
    [3, 4]
])

determinant = np.linalg.det(A)

print(determinant)
```

---

## 1️⃣6️⃣ Matrix Inverse

### `np.linalg.inv()`

Used to calculate the inverse of a square matrix.

Example:

```python
inverse = np.linalg.inv(A)

print(inverse)
```

The inverse of a matrix is useful in linear algebra and mathematical computations.

---

# 💼 Mini Projects

## 💰 Expense Tracker

A practical data analysis project built using only NumPy.

The expense data is organized using a multidimensional NumPy array.

### Features Implemented

- Calculate total monthly expense
- Calculate average daily spending
- Find the highest spending day
- Find the lowest spending day
- Find days where spending exceeded a given budget
- Count the number of days exceeding the budget
- Perform category-wise expense analysis
- Compare spending between categories
- Find highest spending category
- Find lowest spending category
- Find all expenses greater than a specific value
- Find days where Food expenses exceeded a limit
- Find days where Shopping expenses were below a limit
- Replace expenses above a certain limit
- Apply discount percentage to a particular category

### NumPy Concepts Used

```text
✓ 2D Arrays
✓ np.sum()
✓ np.mean()
✓ np.max()
✓ np.min()
✓ np.argmax()
✓ np.argmin()
✓ Axis Operations
✓ Boolean Indexing
✓ Array Filtering
✓ Array Modification
✓ Broadcasting
✓ Statistical Analysis
```

---

## 🎓 Student Data Analysis

A simple data analysis project using NumPy arrays to analyze student marks.

### Operations Performed

- Store student marks in a NumPy array
- Calculate student-wise averages
- Calculate subject-wise averages
- Find the top-performing student
- Find highest marks
- Find lowest marks
- Compare student performance

### NumPy Concepts Used

- 2D arrays
- `np.mean()`
- `np.max()`
- `np.min()`
- `np.argmax()`
- `axis=0`
- `axis=1`

---

# 📁 Repository Structure

```text
numpy-data-analytics-project/
│
├── Advance_Numpy.py
│   └── Practice of NumPy functions and matrix operations
│
├── ExpenseTracker.py
│   └── Expense analysis project using NumPy
│
├── student.py
│   └── Student data analysis using NumPy
│
├── concepts_practiced.md
│   └── Summary of NumPy concepts practiced
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md
    └── Complete project documentation
```

---

# 🛠️ Technologies Used

- Python
- NumPy

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/Jagriti-student/numpy-data-analytics-project.git
```

## Move to Project Directory

```bash
cd numpy-data-analytics-project
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

Or install NumPy directly:

```bash
pip install numpy
```

---

# ▶️ How to Run

Run the advanced NumPy practice file:

```bash
python Advance_Numpy.py
```

Run the Expense Tracker:

```bash
python ExpenseTracker.py
```

Run Student Data Analysis:

```bash
python student.py
```

---

# 🧠 Key Concepts Learned

Through this repository, I practiced:

```text
✓ NumPy Introduction
✓ NumPy Arrays
✓ Array Creation
✓ Zeros and Ones Arrays
✓ Range Arrays
✓ Linspace
✓ Identity Matrix
✓ Random Arrays
✓ Array Properties
✓ Indexing
✓ Slicing
✓ 2D Arrays
✓ Reshaping
✓ Flattening
✓ Ravel
✓ Mathematical Operations
✓ Vectorized Operations
✓ Broadcasting
✓ Boolean Indexing
✓ Array Filtering
✓ Array Modification
✓ Statistical Operations
✓ Axis Operations
✓ Sorting
✓ Argsort
✓ Matrix Operations
✓ Matrix Multiplication
✓ Matrix Transpose
✓ Determinant
✓ Matrix Inverse
✓ Data Analysis Using NumPy
```

---

# 🎯 Learning Approach

My learning approach for NumPy:

```text
Learn the Concept
       ↓
Practice with Small Examples
       ↓
Understand Array Operations
       ↓
Practice Without Traditional Loops
       ↓
Apply Concepts to Real Data
       ↓
Build Mini Projects
       ↓
Improve Understanding Through Practice
```

---

# 💡 Key Takeaways

Some important things I learned while practicing NumPy:

- NumPy arrays are efficient for numerical computation.
- Vectorized operations reduce the need for traditional loops.
- Broadcasting makes array operations easier.
- Boolean indexing is useful for filtering data.
- The `axis` concept is essential for multidimensional data analysis.
- NumPy provides powerful statistical functions.
- Matrix operations can be performed efficiently using NumPy.
- Multidimensional arrays can represent real-world datasets.
- Practical projects help in understanding theoretical concepts better.

---

# 🌱 Learning Journey

This repository represents my hands-on learning journey with NumPy.

Rather than only reading concepts, I focused on:

> **Learning → Practicing → Experimenting → Building**

The goal of this repository is to build a strong foundation in numerical computing and data analysis using Python.

I will continue updating this repository as I learn more concepts and build more projects.

---

## ⭐ If You Find This Repository Helpful

Feel free to explore the code and concepts.

If you find this repository useful, consider giving it a ⭐!

---

### 👩‍💻 Author

**Jagriti**

B.Tech Computer Science Student | Python | Data Analytics | Aspiring Software Developer

---

> **"The best way to learn is by practicing and building." 🚀**