import numpy as np

# define the array
my_array = np.array([[0, 1, 2], [3, 4, 5]])

# compute the sum of the diagonal elements
sum_of_diagonal = np.trace(my_array)

# print the array and the sum of the diagonal elements
print("Array:\n", my_array)
print("Sum of the diagonal elements: ", sum_of_diagonal)