from graficos import *
from funciones import *

matriz_2D = np.array([[1,0], [0,1]])

class Linea2D(Linea, Graficable):
    @override
    def draw(self, canvas) -> None:
        glBegin(GL_LINES)
        glColor3fv(self.color  / 255)
        glVertex2fv(transformacion(matriz_2d, self.start))
        glVertex2fv(transformacion(matriz_2d, self.end))
        glEnd()
        

class Vector2D(GraficoCompuesto):
    def __init__(self, start: Sequence[float], vector: Sequence[float], color: Sequence[float]):
        super().__init__(color)
        self.start = np.array(start)
        self.vector = np.array(vector)
    
    @override
    def load_components(self) -> None:
        punta = self.start+self.vector
        linea = Line2D(self.start, punta, self.color)
        colas = recolectar_colas_vector2D(self.vector)
        cola_1 = Line2D(punta, punta+colas[0], self.color)
        cola_2 = Line2D(punta, punta+colas[1], self.color)
        self.add_components(linea, cola1, cola2)


class Polygon2D(Polygon):
    @override
    def load_components(self) -> None:
        a=np.array([1,2])
        for i in range(len(self.points)-1):
            point = self.points[i]
            next_point = self.points[i+1]
            self.add_components(Line(point, next_point, self.color))
        if self.closed:
           self.add_components(Line(next_point, self.points[0], self.color))
    
    @override
    def draw_filled(self) -> None:
        glBegin(GL_POLYGON)
        glColor3fv(self.color  / 255)
        for point in self.points:
            glVertex2fv(transformacion(matriz_2d, point))
        glEnd()


class Curva2D(Polygon2D):
    def __init__(self, func: FuncionUnaVar, color: Sequence[float], fill=False) -> None:
        self.func = func
        self.fill = fill
        super().__init__(self.func.get_points(), self.color, self.fill, False)


class Circulo2D(Curva2D):
    def __init__(self, centro: Sequence[float], radio: float, color: Sequence[float], fill=False) -> None:
        self.radio = radio
        self.centro = np.array(centro)
        func = FuncionParametricaUnaVar(range1(0,2*np.pi,100), lambda t: np.array([
            self.centro[0]+radio*np.cos(t), 
            self.centro[1]+radio*np.sin(t)]))
        super().__init__(func, color, fill)


class Point2D(Circulo2D):
    def __init__(self, coord: Sequence[float], color: Sequence[float]):
        super(coord, 5, color, fill=True)