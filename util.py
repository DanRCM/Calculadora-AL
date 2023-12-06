from typing import Callable, Sequence
import numpy as np

matriz_2D = np.array([[1,0], [0,1]])
matriz_rotacion_2d = lambda t: np.array([[np.cos(t), -np.sin(t)],
                                         [np.sin(t), np.cos(t)]])

def override(func: Callable) -> Callable:
    return func

def polar_to_cartesian(point: Sequence[float]) -> np.ndarray:
    t,r = point
    return np.array([r*np.cos(t), r*np.sin(t)]).T

def transformacion(matriz: np.ndarray, point: Sequence) -> np.ndarray:
    return np.matmul(matriz, point)

def rotacion2D(point: Sequence[float], theta: float) -> np.ndarray:
    return transformacion(matriz_rotacion_2d(theta), point)
    
def recolectar_colas_vector2D(vector: np.ndarray) -> np.ndarray:
    if vector[0] == 0 and vector[1] == 0:
        return vector
    u = -vector/np.linalg.norm(vector)
    cola_1 = rotacion2D(u, np.pi/4)
    cola_2 = rotacion2D(u, -np.pi/4)
    return cola_1, cola_2
    

