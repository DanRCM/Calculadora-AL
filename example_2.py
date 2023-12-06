import graficos2d
from graficos2d import *

#Se crea el plano
plano = Plano2D()

#Se crea un dominio para una función
dominio = rango_cartesiano()

#Se crea una función para graficar
funcion = FuncionUnaVar(dominio, lambda x: 3*np.sin(x)**5)

#Se crea una curva
curva = Curva2D(funcion, color = [100, 50, 250])

#se agrega la curva
plano.add_components(curva) 

#Se pone a correr la aplicación
plano.run()