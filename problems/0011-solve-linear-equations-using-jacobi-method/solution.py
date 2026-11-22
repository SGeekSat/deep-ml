import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    A = np.array(A, dtype= float)
    b = np.array(b, dtype = float)
    x = np.zeros(len(b))
    for _ in range(n):
        x_new = np.zeros_like(x)
        
        for i in range(len(b)):
            sum_other = np.sum(A[i]*x)-A[i,i]*x[i]
            x_new[i]= (b[i]-sum_other)/A[i,i]
        x = x_new

    

    return np.round(x,4).tolist()