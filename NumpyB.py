
import numpy as np

# define the square array
square_arr = np.array([[3, -2], [1, 0]])

# compute the eigenvalues and right eigenvectors
eigvals, eigvecs = np.linalg.eig(square_arr)

# print the eigenvalues and right eigenvectors
print("Eigenvalues: ", eigvals)
print("Right Eigenvectors: \n", eigvecs)