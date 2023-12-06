import graficos2d
from graficos2d import *

#Se crea el plano
plano = Plano2D()

#Se crea un dominio para una función
dominio = range1(start = 0, end = 10*np.pi, slices = 1000)

#Se crea una función para graficar
funcion = FuncionPolar(dominio, lambda t: 4*np.sin(1.2*t)**2 + 4*np.cos(6*t)**3)

#Se crea una curva
curva = Curva2D(funcion, color = [180, 200, 50])

#se agrega la curva
plano.add_components(curva) 

#Se pone a correr la aplicación
plano.run()