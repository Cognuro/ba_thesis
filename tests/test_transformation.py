import numpy as np
from unittest import TestCase

t1 = np.array([[-0.413957, 0.836516, -0.358998],
                        [0.875989, 0.258819, -0.407009],
                        [-0.247554, -0.482963, -0.839919]])

t0 = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 1],
               [0, 0, 0, 1]])

t3 = np.array([[0, -0.906890, 0.421367],
               [1, 0, 0],
               [0, 0.4213567, 0.906]])

totalTransformation = t1.dot(t3)

la1, la2, la3 = 274.281, 225, -3.281

t3_alternative = np.array([[0, 0.906890, -0.421367, 0],
                          [1, 0, 0, 0],
                          [0, 0.4213567, 0.906, 0],
                          [0, 0, 0, 1]])

det_t1 = np.linalg.det(t1)
print(det_t1)
