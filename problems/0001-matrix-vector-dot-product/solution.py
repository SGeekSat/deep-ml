import numpy as np
a = np.array([[1, 2], [2, 4]])
b = np.array([1, 2])
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    a = np.array(a)
    b = np.array(b)
    if a.ndim != 2 and b.ndim !=1:
        return -1
    if a.shape[1] != len(b):
        return -1
    product = np.dot(a,b)
    return product

    