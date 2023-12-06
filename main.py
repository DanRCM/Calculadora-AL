import graficos2d
from graficos2d import *

plano = Plano2D()
l = Vector2D([1,1],[2,3], [100,50,250])
f = FuncionPolar(range1(0,2*np.pi,100), lambda x: 3+np.sin(10*x)/5)
q = Curva2D(f,[50,100,150])
p = Point2D([3,3],[70,180,100])
plano.add_components(l,q,p)
plano.run()