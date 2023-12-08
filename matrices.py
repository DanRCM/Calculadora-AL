import numpy as np

a = np.array([[0,0],
              [0,1],
              [0,2],
              [1,0],
              [1,1],
              [1,2],
              [2,0],
              [2,1],
              [2,2]])

print(np.array(np.split(a,3)))