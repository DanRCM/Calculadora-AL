from graficos import *
from funciones import *

matriz_3D = np.array([[1,0,0], [0,1,0], [0,0,1]])

class Linea3D(Linea):
    @override
    def draw(self) -> None:
        glBegin(GL_LINES)
        glColor3fv(self.color  / 255)
        glVertex3fv(transformacion(matriz_3D, self.start))
        glVertex3fv(transformacion(matriz_3D, self.end))
        glEnd()


class Vector3D(GraficoCompuesto):
    def __init__(self, start: Sequence[float], vector: Sequence[float], color: Sequence[float]):
        self.start = np.array(start)
        self.vector = np.array(vector)
        super().__init__(color)
    
    @override
    def load_components(self) -> None:
        punta = self.start+self.vector
        linea = Linea3D(self.start, punta, self.color)
        magnitud = np.linalg.norm(self.vector)
        u = self.vector/magnitud
        circulo = self.start + (magnitud-0.5)*u+recolectar_circulo_vector3D(self.vector)
        self.add_components(linea)
        for i in range(len(circulo)-1):
            vertices = [circulo[i], circulo[i+1],punta]
            self.add_components(Polygon3D(vertices, self.color, True))
        
        
class Polygon3D(Polygon):
    @override
    def load_components(self) -> None:
        for i in range(len(self.points)-1):
            point = self.points[i]
            next_point = self.points[i+1]
            self.add_components(Linea3D(point, next_point, self.color))
        if self.closed:
           self.add_components(Linea3D(next_point, self.points[0], self.color))
    
    @override
    def draw_filled(self) -> None:
        glBegin(GL_POLYGON)
        glColor3fv(self.color  / 255)
        for point in self.points:
            glVertex3fv(transformacion(matriz_3D, point))
        glEnd()

class Curva3D(Polygon3D):
    def __init__(self, func: FuncionParametricaUnaVar, color: Sequence[float], fill=False) -> None:
        self.func = func
        super().__init__(self.func.get_points(), color, fill, False)


class Superficie(GraficoCompuesto):
    def __init__(self, func: FuncionDosVar, color: Sequence[float], border=True) -> None:
        self.func = func
        self.border = border
        super().__init__(color)
    
    @override
    def load_components(self) -> None:
        rebanadas = int(len(self.func.dominio)**0.5)
        points = np.array(np.split(self.func.get_points(),rebanadas))
        for i in range(rebanadas-1):
            for j in range(rebanadas-1):
                vertices = [points[i,j], points[i,j+1], points[i+1,j+1], points[i+1,j]]
                if self.border:
                    self.add_components(Polygon3D(vertices, [0,0,0], False))
                self.add_components(Polygon3D(vertices, self.color, True))


class Esfera(Superficie):
    def __init__(self, centro: Sequence[float], radio: float, color: Sequence[float], border=True) -> None:
        self.radio = radio
        self.centro = np.array(centro)
        func = FuncionParametricaDosVar(range2([0,2*np.pi],[0,np.pi],10), lambda t,f: np.array([
            self.centro[0]+radio*np.sin(f)*np.cos(t), 
            self.centro[1]+radio*np.sin(f)*np.sin(t),
            self.centro[2]+radio*np.cos(f)]))
        super().__init__(func, color, border)


class Point3D(Esfera):
    def __init__(self, coord: Sequence[float], color: Sequence[float]):
        super().__init__(coord, 0.05, color, border=False)
    
class Espacio3D(SuperContainer):
    def __init__(self, color_axisas: Sequence[Sequence[float]]=[[255,0,0], [0,255,0], [255,255,255]], color: Sequence[float]=[0,0,0]) -> None:    
        super().__init__(color_axisas, color)
    
    @override    
    def load_components(self) -> None:
        self.axis_x = Vector3D([-3, 0, 0], [6, 0, 0], self.axes_color[0])
        self.axis_y = Vector3D([0, -3, 0], [0, 6, 0], self.axes_color[1])
        self.axis_z = Vector3D([0, 0, -3], [0, 0, 6], self.axes_color[2])
        self.add_components(self.axis_x, self.axis_y,self.axis_z)
    
    @override
    def config_gl(self) -> None:
        glEnable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glMatrixMode(GL_MODELVIEW)
        gluPerspective(100, (self.size[0] / self.size[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        glRotatef(-60,1,0,0)
        glRotatef(-135,0,0,1)
        glScalef(1,1,1)