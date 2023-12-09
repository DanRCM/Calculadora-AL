import graficos3d
from graficos3d import *

#Se crea el espacio
espacio = Espacio3D()

#Se crea un dominio para una función
dominio = range2([0,2*np.pi], [0,2*np.pi], 30)

#Se crea una función para graficar
funcion = FuncionParametricaDosVar(dominio, lambda u,v: np.array([(2+np.sin(v))*np.cos(u),
                                                                  (2+np.sin(v))*np.sin(u),
                                                                  u+np.cos(v)-3]))

#Se crea una curva
superficie= Superficie(funcion, color = [200, 50, 100])

#Se añaden al espacio
espacio.add_components(superficie)

#Se pone a correr la aplicación
espacio.run()