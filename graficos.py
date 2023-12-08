from abc import ABC, abstractmethod
from typing import Sequence
import numpy as np
from util import override
import pygame as py
from pygame.locals import *
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Graficable(ABC):
    def __init__(self, color: Sequence[float]) -> None:
        self.color = np.array(color)
    
    @abstractmethod
    def draw(self) -> None:...


class GraficoCompuesto(Graficable, ABC):
    def __init__(self, color: Sequence[float]) -> None:
        super().__init__(color)
        self.componentes = []
        self.load_components()
    
    def add_components(self, *grafico: Graficable) -> None:
        self.componentes += list(grafico)
        
    @override
    def draw(self) -> None:
        for graficable in self.componentes:
            graficable.draw()
            
    @abstractmethod
    def load_components(self) -> None:...
    

class Linea(Graficable, ABC):
    def __init__(self, start: Sequence[float], end: Sequence[float], color: Sequence[float]) -> None:
        super().__init__(color)
        self.start = np.array(start)
        self.end = np.array(end)
    
    @abstractmethod
    def draw(self) -> None:...
    
    
class Polygon(GraficoCompuesto, ABC):
    def __init__(self, points: Sequence[Sequence[float]], color: Sequence[float], fill=False, closed=True) -> None:
        self.points = np.array(points)
        self.fill = fill
        self.closed = closed
        super().__init__(color)
    
    @override
    def draw(self) -> None:
        if self.fill:
            self.draw_filled()
        else:
            super().draw()
            
    @abstractmethod
    def draw_filled(self) -> None:...
        
    @abstractmethod
    def load_components(self) -> None:...

class SuperContainer(GraficoCompuesto, ABC):
    def __init__(self, color_axisas: Sequence, color: Sequence[int]) -> None:
        self.axes_color = color_axisas
        py.init()
        super().__init__(color) 
        self.running = True
        self.size = (width, height) = (1300, 700)
        self.screen = py.display.set_mode(self.size, DOUBLEBUF | OPENGL)
        self.config_gl()
    
    def run(self) -> None:
        while self.running:
            for event in py.event.get():
                if event.type == QUIT:
                    sys.exit()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.draw()
            py.display.flip()
            py.time.wait(10)
            
    @override
    def add_components(self, *components: Graficable) -> None:
        for componente in components:
            self.componentes.insert(0,componente)
  
    @abstractmethod
    def load_components(self) -> None: ...
    
    @abstractmethod
    def config_gl(self) -> None: ...