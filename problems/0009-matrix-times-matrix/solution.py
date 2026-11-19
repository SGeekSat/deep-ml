import numpy as np
A = np.array([[1,2],[2,4]])
B = np.array([[2,1],[3,4]])
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

              
    a = np.array(a)
    b= np.array(b)  
    if a.shape[1] != b.shape[0]:
        
        return -1  
    c = np.dot(a,b)      
    return c.tolist()