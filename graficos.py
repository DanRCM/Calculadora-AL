from abc import ABC,abstractclassmethod
from typing import Sequence
import numpy as np
from util import override

class Graficable(ABC):
    def __init__(self, color: Sequence[float]) -> None:
        self.color = np.array(color)
    
    @abstractclassmethod
    def draw(self, canvas) -> None:...


class GraficoCompuesto(Graficable, ABC):
    def __init__(self, color: Sequence[float]) -> None:
        super().__init__(color)
        self.componentes = []
        self.load_components()
    
    def add_components(self, *grafico: Graficable) -> None:
        self.componentes += list(grafico)
        
    @override
    def draw(self, canvas) -> None:
        for graficable in self.componentes:
            graficable.draw(canvas)
            
    @abstractclassmethod
    def load_components(self) -> None:...
    

class Linea(Graficable, ABC):
    def __init__(self, start: Sequence[float], end: Sequence[float], color: Sequence[float]) -> None:
        super().__init__(color)
        self.start = np.array(start)
        self.end = np.array(end)
    
    @abstractclassmethod
    def draw(self, canvas) -> None:...
    
    
class Polygon(GraficoCompuesto, ABC):
    def __init__(self, points: Sequence[Sequence[float]], color: Sequence[float], fill=False, closed=True) -> None:
        self.points = np.array(points)
        self.fill = fill
        self.closed
        super().__init__(color)
    
    @override
    def draw(self) -> None:
        if self.fill:
            self.draw_filled()
        else:
            super().draw()
            
    @abstractclassmethod
    def draw_filled(self) -> None:...
        
    @abstractclassmethod
    def load_components(self) -> None:...
