import numpy as np

"""
1.	Compute the multiplication of the following matrices:
[[1, 0], [0, 1]]
[[1, 2], [3, 4]]
"""
m1 = [
        [1, 0],
        [0, 1]
    ]
m2 = [
        [1, 2],
        [3, 4]
    ]

r = np.matmul(m1, m2)
print('\nexercise 1\n', r)

"""
2.	Generate an array of length 3n filled with the cyclic pattern 1, 2, 3.
"""

n = 4
x = [1, 2, 3]
a = np.repeat(x, n)
print('\nexercise 2 repeat\n', a)
b = np.tile(x, n)
print('\nexercise 2 tile\n', b)  # a second alternative presented in case of misunderstanding "cyclic pattern"

"""
3.	Create a 10×10 matrix of zeros and then 
    "frame" it with a border of ones.
"""

z = np.zeros((10, 10))  # a matrix filled with zeroes is created
print('\nexercise 3 zeros\n', z)
u = np.ones((12, 12))  # a matrix filled with number one is created
print('\nexercise 3 ones\n', u)
u[1:11, 1:11] = z  # we superimpose z matrix over u matrix
print('\nexercise 3 new ones\n', u)

"""
4.	Create a random 3×5 array using the np.random.rand(3, 5) 
    function and compute: the sum of all the entries, the sum 
    of the rows and the sum of the columns. (many Numpy functions 
    have an optional axis= argument!)
"""
r = np.random.rand(3, 5)
print('\nexercise 4 random 3x5\n', r)
print('\nexercise 4 sum all\n', np.sum(r))
print('\nexercise 4 sum all by row\n', np.sum(r, axis=0))
print('\nexercise 4 sum all by cols\n', np.sum(r, axis=1))


"""
5.	Given the following arrays representing logical values (0 = False, 1 = True) 
compute the logical AND and logical OR operations for every pair of values of 
the two arrays: [1, 1, 0, 0] [1, 0, 1, 0] 
Hint: you may need to set the data type (dtype) of the array's elements to 'bool'
"""
d1 = np.array([1, 1, 0, 0])  # matrix is created
d2 = np.array([1, 0, 1, 0])
print('exercise 5 arrays\n', d1, '\n', d2)
b1 = d1.astype(bool)  # The arrays are transformed into boolean
b2 = d2.astype(bool)
print('\nexercise 5 bool arrays\n', b1, '\n', b2)
print('\nlogical AND', np.logical_and(b1, b2))  # we use the AND and OR numpy functions and print them
print('\nlogical OR', np.logical_or(b1, b2))

"""
6.	Find indices of non-zero elements from [1, 2, 0, 0, 4, 0]
"""

e = np.array([1, 2, 0, 0, 4, 0])
print('exercise 6')
print('\narray items\n', e)
print('\narray indices\n', np.nonzero(e))  # we use the numpy nonzero function and print

"""
7.	Create a 8×8 array with random values and find minimum and maximum value
"""

r = np.random.rand(8, 8)
# we use the random.rand function to create the array specified
# and then use np.min, which gets a minimum value along a specified axis.
print('\nexercise 7 random 8x8\n', r)
print('\nexercise 7 minimum all\n', np.min(r))
print('\nexercise 7 maximum all\n', np.max(r))

"""
8.	Create a 8×8 array with random natural values from the range (1-100) 
on the diagonal, other values should be 0. 
Hint: You can use numpy's 'eye' function.
"""
n = 8
m = np.eye(n, n) # we use the eye function to create the desired matrix
print('mat eye\n', m)
# we use the radint function to create random integers between the specified limits
r = np.random.randint(1, 100, 8)
print('random array\n', r)
np.fill_diagonal(m, r)
print('mat updated\n', m)


"""
9.	Write a function which creates an n×n matrix with
(i,j)-entry equal to i+j.
"""

def create_matrix(n):
    z = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            z[i, j] = i + j
    return z

m = create_matrix(3)
print('\nmatrix\n', m)

"""
10.	Write a function which creates an n×n matrix with rows 
having subsequent values multiplied by the row's number. 
For example for n = 4: 
[
    [0, 1, 2, 3], 
    [0, 2, 4, 6], 
    [0, 3, 6, 9], 
    [0, 4, 8, 12]
]
"""

def create_matrix2(n):
    z = np.zeros((n, n), dtype=int)  # we create a zero filled matrix of integer type
    for i in range(n):  # cycle for lines 0,1,2,3,...   we set up the conditions for the formula
        # print('i=', i)
        for j in range(n): # cycle for columns 0,1,2,3,
            # print('j=', j)
            z[i, j] = j + i * j
            # print('z[i, j]=', z[i, j])
    return z

m = create_matrix2(4)
print('\nmatrix\n', m)
