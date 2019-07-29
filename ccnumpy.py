##
This script is a crash course on numpy
##
import numpy as np

my_list = [1,2,3]

arr = np.array(my_list)

print(type(arr))

# array 
print(np.arange(0,10))

# array with steps
print(np.arange(0,9,3))

# array of zeros - one dimensional array
print(np.zeros(5))

# array of zeros - two dimensional arrya
print(np.zeros((3,4)))

# array of ones - one dimensional array
print(np.ones(6))

# array of ones - two dimensional array
print(np.ones((3,3)))

# array of linearly spaced elements
print(np.linspace(0, 10, 10))

# random number generation
print(np.random.randint(0,100))

# random number with seed - generate the same random numbers
np.random.seed(101)
s = np.random.randint(0,100,10)

print(s)
print(s.max())
print(s.min())
print(s.mean())

# return the index of max
print(s.argmax())

# reshape an array - elements should fit evenly
print(s.reshape(2,5))

# indexing

mat = np.arange(0,100).reshape(10,10)
print(mat)
print(mat[0,1])
print(mat[0:3,0])
print(mat[0:3,0:3])

# boolean operations
print(mat > 50)

# boolean masking
my_filter = mat > 50
print(mat[my_filter])
