from modelo.Punto import*
from modelo.Rectangulo import*
import pickle
puntos=[Punto(2,3),Punto(5,5),Punto(-3, -1),Punto(0,0)]
#Leer archivo
f = open('puntos.pckl','rb')
puntos = pickle.load(f)
f.close()
for p in puntos:
    print(p)

A = puntos[0]
B = puntos[1]
C = puntos[2]
D = puntos[3]

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

R = Rectangulo(A, B)
R.base()
R.altura()
R.area()