class Clase1:
    def metodo1(self):
        print("Hola soy el metodo de la clase 1")
class Clase2:
    def metodo2(self):
        print("Hola soy el metodo de la clase 2")
class Clase3(Clase1,Clase2):
    def metodo3(self):
        print("Hola soy el metodo de la clase 3")

c=Clase3()
c.metodo1()
c.metodo2()
c.metodo3()