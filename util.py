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

def cilindro_to_cartesian(point: Sequence[float]) -> np.ndarray:
    t,r,z = point
    return np.array([r*np.cos(t), r*np.sin(t), z])

def esfera_to_cartesian(point: Sequence[float]) -> np.ndarray:
    t,f,p = point
    return np.array([p*np.sin(f)*np.cos(t), p*np.sin(f)*np.sin(t), p*np.cos(f)])

def transformacion(matriz: np.ndarray, point: Sequence) -> np.ndarray:
    return np.matmul(matriz, point)

def rotacion2D(point: Sequence[float], theta: float) -> np.ndarray:
    return transformacion(matriz_rotacion_2d(theta), point)
    
def recolectar_colas_vector2D(vector: np.ndarray) -> np.ndarray:
    if vector[0] == 0 and vector[1] == 0:
        return vector
    u = -vector/(2*np.linalg.norm(vector))
    cola_1 = rotacion2D(u, np.pi/4)
    cola_2 = rotacion2D(u, -np.pi/4)
    return cola_1, cola_2
    
def recolectar_circulo_vector3D(vector: np.ndarray) -> np.ndarray:
    if vector[2] == 0:
        u1,u2 = np.array([1,0,0]) , np.array([0,1,0])
    else:
        x,y,z = vector
        a = z / (x**2 + z**2) ** 0.5
        c = -a*x / z
        u1 = np.array([a,0,c])
        v2 = np.cross(vector, u1)
        u2 = v2/np.linalg.norm(v2)
    m = np.array([u1,u2]).T
    r = lambda t: np.matmul(m, np.array([np.cos(t),np.sin(t)]))
    muestras = np.linspace(0,2*np.pi,100)

    circulo = r(muestras).T/5
    return circulo
     
