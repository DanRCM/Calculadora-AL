import graficos2d
from graficos2d import *

#Se crea el plano
plano = Plano2D()

#Se crea un dominio para una función
dominio = rango_polar()

#Se crea una función para graficar
funcion = FuncionParametricaUnaVar(dominio, lambda t: 3*np.array([np.cos(t) + np.cos(20*t), np.sin(t) + np.sin(20*t)]))

#Se crea una curva
curva = Curva2D(funcion, color = [70, 150, 200])

#se agrega la curva
plano.add_components(curva) 

#Se pone a correr la aplicación
plano.run()