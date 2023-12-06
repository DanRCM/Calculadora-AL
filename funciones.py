from abc import ABC, abstractmethod
from typing import Sequence, Callable
import numpy as np
from util import *

def range1(start: float, end: float, slices: int):
    return np.linspace(start, end, slices)

def rango_cartesiano():
    return range1(-20,20,1000)

def rango_polar():
    return range1(0, 2*np.pi, 1000)

def range2(rango1: Sequence[float], rango2: Sequence[float], slices: int):
    x = range1(*rango1, slices)
    y = range1(*rango2, slices)
    X,Y = np.meshgrid(x,y)
    return np.column_stack((X.ravel(), Y.ravel()))

class Funcion(ABC):
    def __init__(self, dominio: Sequence, func: Callable) -> None:
        self.dominio = np.array(dominio)
        self.func = func
        
    @abstractmethod
    def load_range(self) -> np.ndarray: ...
    
    @abstractmethod
    def get_points(self) -> np.ndarray: ...

class FuncionUnaVar(Funcion):
    @override
    def load_range(self) -> np.ndarray:
        rango = self.func(self.dominio)
        if isinstance(rango, int) or isinstance(rango, float):
            return np.full(len(self.dominio), rango)
        else:
            return rango
    
    @override
    def get_points(self) -> np.ndarray:
        return np.column_stack((self.dominio, self.load_range()))


class FuncionParametricaUnaVar(FuncionUnaVar):
    @override
    def load_range(self) -> np.ndarray:
        try:
            rango = self.func(self.dominio).T
        except:
            rango = np.array(list(map(self.func, self.dominio.T)))
        
        if len(rango.shape) == 1:
            shape =(self.dominio.shape[0],2)
            return np.full(shape, rango)
        else:
            return rango
    
    @override
    def get_points(self) -> np.ndarray:
        return self.load_range()


class FuncionPolar(FuncionUnaVar):
    @override
    def load_range(self) -> np.ndarray:
        rango = self.func(self.dominio)
        if isinstance(rango, int) or isinstance(rango, float):
            return np.full(len(self.dominio), rango)
        else:
            return rango
        
    @override
    def get_points(self) -> np.ndarray:
        points = super().get_points()
        return polar_to_cartesian(points.T)
    

class FuncionDosVar(Funcion):
    @override
    def load_range(self) -> np.ndarray:
        rango = self.func(*self.dominio.T)
        if isinstance(rango, int) or isinstance(rango, float):
            shape = self.dominio.shape[0]
            return np.full(shape, rango)
        else:
            return rango
    
    @override
    def get_points(self) -> np.ndarray:
        return np.column_stack((self.dominio,self.load_range()))


class FuncionParametricaDosVar(FuncionDosVar):
    @override
    def load_range(self) -> np.ndarray:
        try:
            rango = self.func(*self.dominio.T).T
        except:
            rango = np.array(list(map(self.func, *self.dominio.T)))
        if len(rango.shape) == 1:
            shape = self.dominio.shape
            return np.full(shape, rango)
        else:
            return rango
    
    @override
    def get_points(self) -> np.ndarray:
        return self.load_range()
        

class FuncionCilindrica(FuncionDosVar):
    @override
    def load_range(self) -> np.ndarray:
        rango = self.func(*self.dominio.T)
        if isinstance(rango, int) or isinstance(rango, float):
            shape = self.dominio.shape[0]
            return np.full(shape, rango)
        else:
            return rango
        
    @override
    def get_points(self) -> np.ndarray:
        points = super().get_points()
        return cilindro_to_cartesian(points.T).T


class FuncionEsferica(FuncionDosVar):
    @override
    def load_range(self) -> np.ndarray:
        rango = self.func(*self.dominio.T)
        if isinstance(rango, int) or isinstance(rango, float):
            shape = self.dominio.shape[0]
            return np.full(shape, rango)
        else:
            return rango
        
    @override
    def get_points(self) -> np.ndarray:
        points = super().get_points()
        return esfera_to_cartesian(points.T).T