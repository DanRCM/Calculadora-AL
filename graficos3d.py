from graficos import *
from funciones import *

matriz_3D = np.array([[1,0,0], [0,0,1]])

class Linea3D(Linea):
    @override
    def draw(self) -> None:
        glBegin(GL_LINES)
        glColor3fv(self.color  / 255)
        glVertex3fv(transformacion(matriz_3D, self.start))
        glVertex3fv(transformacion(matriz_3D, self.end))
        glEnd()


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
            glVertex3fv(transformacion(matriz_2D, point))
        glEnd()
