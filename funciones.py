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

class Funcion:
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
        return self.func(self.dominio).T
    
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