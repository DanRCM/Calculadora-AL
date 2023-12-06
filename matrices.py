import numpy as np

matriz_2D = np.array([[1,0], [0,1]])
matriz_rotacion_2d = lambda t: np.array([[np.cos(t), -np.sin(t)],
                                         [np.sin(t), np.cos(t)]])