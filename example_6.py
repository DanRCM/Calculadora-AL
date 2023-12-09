import graficos3d
from graficos3d import *

#Se crea el espacio
espacio = Espacio3D()

#Se crea un vector
vector = Vector3D(start=[0,0,0], vector=[-1,2,-2], color=[150,100,200])

#Se crea un punto
point = Point3D(coord=[3,2,1], color=[250,150,50])

#Se añaden al espacio
espacio.add_components(vector, point)

#Se pone a correr la aplicación
espacio.run()