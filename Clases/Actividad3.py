import math

class Punto:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))
            
    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(self, p, p.x - self.x, p.y - self.y) )
        
    def distancia(self, p):
        d = math.sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
        print("La distancia entre los puntos {} y {} es {}".format(self, p, d))
        

class Rectangulo:
    
    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
        
    def base(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        print("La base del rectángulo es {}".format( self.base ) )
        
    def altura(self):
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        print("La altura del rectángulo es {}".format( self.altura ) )
        
    def area(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        self.area = self.base * self.altura
        print("El área del rectángulo es {}".format( self.area ) )
        
    
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

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