import graficos2d
from graficos2d import *

# u,v serán los vectores base
u = np.array([1,1])
v = np.array([-3,1])

#se crea la matriz de transformación con los vectores base
graficos2d.matriz_2D = np.array([u,v]).T

#Se crea el plano
plano = Plano2D()

#Se crean los gráficos para los vectores base
#Solo se escriben sus coordenadas [1,0] [0,1] porque la transformación se hace internamente
vector_base_u = Vector2D([0,0], [1,0], color = [250, 0, 0])
vector_base_v = Vector2D([0,0], [0,1], color = [0, 250, 0])

#Se crea un dominio para una función
dominio = rango_cartesiano()

#Se crea una función para graficar
funcion = FuncionUnaVar(dominio, lambda x: np.sin(x))

#Se crea una curva
curva = Curva2D(funcion, color = [200, 150, 100])

#se agregan los vectores base y la curva
plano.add_components(vector_base_u, vector_base_v, curva) 

#Se pone a correr la aplicación
plano.run()