import numpy as np

A = np.array([4,1,-2,-3,2,1,2,1,-1]).reshape(3,3)
b = np.array([5,3,8])
x = np.linalg.inv(A).dot(b)

print(x)