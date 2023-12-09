import graficos3d
from graficos3d import *

#Se crea el espacio
espacio = Espacio3D()

#Se crea un dominio para una función
dominio = range1(0,2*np.pi,1000)

#Se crea una función para graficar
funcion = FuncionParametricaUnaVar(dominio, lambda t: 0.5*np.array([(4+np.sin(20*t))*np.cos(t),
                                                                (4+np.sin(20*t)*np.sin(t))*np.sin(t),
                                                                np.cos(20*t)]))

#Se crea una curva
curva = Curva3D(funcion, color = [100, 50, 250])

#Se añaden al espacio
espacio.add_components(curva)

#Se pone a correr la aplicación
espacio.run()