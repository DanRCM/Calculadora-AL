import graficos2d
from graficos2d import *

#Se crea el plano
plano = Plano2D()

#punto con la coordenada [3,3]
point = Point2D(coord = [3,3], color = [70,180,100])

#vector que empieza [1,1] y tiene como direccion [2,3]
vector = Vector2D(start = [1,1], vector = [2,3], color = [100,50,250])

#se agrega el punto y el vector al plano
plano.add_components(point, vector) 

#Se pone a correr la aplicación
plano.run()