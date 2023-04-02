import numpy as np

# create the original array
my_array = np.array([1, 2, 3, 4, 5, 6])
print("Original array:\n", my_array)

# reshape the array to 3x2
new_array = np.reshape(my_array, (3, 2))
print("Reshaped array:\n", new_array)
# reshape the array to 2x3
new_array = np.reshape(my_array, (2, 3))

# print the original and reshaped arrays
print("Reshaped array:\n", new_array)