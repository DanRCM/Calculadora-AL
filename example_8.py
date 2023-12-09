import graficos3d
from graficos3d import *

#Se crea el espacio
espacio = Espacio3D()

#Se crea un dominio para una función
dominio = range2([-2,2], [-2,2], 30)

#Se crea una función para graficar
funcion = FuncionDosVar(dominio, lambda x,y: np.sin(y)+np.cos(x))

#Se crea una curva
superficie= Superficie(funcion, color = [150, 250, 100])

#Se añaden al espacio
espacio.add_components(superficie)

#Se pone a correr la aplicación
espacio.run()