import numpy as np
A = np.array([[1, 2],
              [3, 4]])
print(A.T)             # transpose
Amoins=np.linalg.inv(A)  # inverse
print(Amoins)

