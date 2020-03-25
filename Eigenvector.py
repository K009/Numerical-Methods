import numpy
import numpy as np
import scipy.sparse.linalg as linalg
from scipy.sparse.linalg import eigsh

A = np.matrix([[2.0, -1.0, 0.0, 0.0, 1.0],
               [-1.0, 2.0, 1.0, 0.0, 0.0],
               [0.0, 1.0, 1.0, 1.0, 0.0],
               [0.0, 0.0, 1.0, 2.0, -1.0],
               [1.0, 0.0, 0.0, -1.0, 2.0]])

print("Hermitian matrix:")
print(A)

eigen_value = 0.38197

np.set_printoptions(precision=5)
               
vals, vecs = linalg.eigsh(A, k=1, sigma=eigen_value)
print("Eigenvector:")
print(vecs)
print("for eigenvalue:")
print(vals)
