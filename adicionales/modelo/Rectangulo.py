
class Rectangulo:
    
    def __init__(self, pInicial, pFinal):
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