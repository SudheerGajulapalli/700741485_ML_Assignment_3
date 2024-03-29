import numpy as np

# create a random vector of size 15 with integers in the range of 1-20
random_vector = np.random.randint(1, 21, size=15)
print("Before Update:\n",random_vector)
# reshape the array to 3 by 5
random_vector = random_vector.reshape(3, 5)

# print the array shape
print("Array Shape:", random_vector.shape)
print("after Reshape:\n",random_vector)

# replace the max in each row by 0
random_vector[np.arange(len(random_vector)), np.argmax(random_vector, axis=1)] = 0

# print the updated array
print("Updated Array:\n", random_vector)

# create a 2-dimensional array of size 4 x 3
array_2d = np.zeros((4, 3), dtype=np.int32)

# print the shape, type, and data type of the array
print("\nArray Shape:", array_2d.shape)
print("Array Type:", type(array_2d))
print("Array Data Type:", array_2d.dtype)