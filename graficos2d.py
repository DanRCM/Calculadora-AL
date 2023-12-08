from graficos import *
from funciones import *

matriz_2D = np.array([[1,0], [0,1]])

class Linea2D(Linea):
    @override
    def draw(self) -> None:
        glBegin(GL_LINES)
        glColor3fv(self.color  / 255)
        glVertex2fv(transformacion(matriz_2D, self.start))
        glVertex2fv(transformacion(matriz_2D, self.end))
        glEnd()
        

class Vector2D(GraficoCompuesto):
    def __init__(self, start: Sequence[float], vector: Sequence[float], color: Sequence[float]):
        self.start = np.array(start)
        self.vector = np.array(vector)
        super().__init__(color)
    
    @override
    def load_components(self) -> None:
        punta = self.start+self.vector
        linea = Linea2D(self.start, punta, self.color)
        colas = recolectar_colas_vector2D(self.vector)
        cola_1 = Linea2D(punta, punta+colas[0], self.color)
        cola_2 = Linea2D(punta, punta+colas[1], self.color)
        self.add_components(linea, cola_1, cola_2)


class Polygon2D(Polygon):
    @override
    def load_components(self) -> None:
        for i in range(len(self.points)-1):
            point = self.points[i]
            next_point = self.points[i+1]
            self.add_components(Linea2D(point, next_point, self.color))
        if self.closed:
           self.add_components(Linea2D(next_point, self.points[0], self.color))
    
    @override
    def draw_filled(self) -> None:
        glBegin(GL_POLYGON)
        glColor3fv(self.color  / 255)
        for point in self.points:
            glVertex2fv(transformacion(matriz_2D, point))
        glEnd()


class Curva2D(Polygon2D):
    def __init__(self, func: FuncionUnaVar, color: Sequence[float], fill=False) -> None:
        self.func = func
        super().__init__(self.func.get_points(), color, fill, False)


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
        super().__init__(coord, 0.1, color, fill=True)
        
class Grid(GraficoCompuesto):
    def __init__(self, color: Sequence[float]) -> None:
        self.long = 20
        super().__init__(color)
            
    @override
    def load_components(self) -> None:
        for i in range(self.long):
            if i!=0:
                self.add_components(Linea2D([-self.long, i], [self.long, i], self.color))
                self.add_components(Linea2D([-self.long, -i], [self.long, -i], self.color))
                self.add_components(Linea2D([i, -self.long], [i, self.long], self.color))
                self.add_components(Linea2D([-i, -self.long], [-i, self.long], self.color))
            else:
                self.add_components(Linea2D([-self.long, i], [self.long, i], self.color))
                self.add_components(Linea2D([i, -self.long], [i, self.long], self.color))
                
class Plano2D(SuperContainer):
    def __init__(self, color_axisas: Sequence[Sequence[float]]=[[255,255,255], [255,255,255]], color: Sequence[float]=[0,0,0]) -> None:    
        super().__init__(color_axisas, color)
    
    @override    
    def load_components(self) -> None:
        self.grid = Grid([50,50,50])
        self.axis_x = Linea2D([-self.grid.long, 0], [self.grid.long, 0], self.axes_color[0])
        self.axis_y = Linea2D([0, -self.grid.long], [0, self.grid.long], self.axes_color[1])
        self.add_components(self.grid, self.axis_x, self.axis_y)
    
    @override
    def config_gl(self) -> None:
        glEnable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glMatrixMode(GL_MODELVIEW)
        glScalef(0.06,0.108,0.1)
    
    