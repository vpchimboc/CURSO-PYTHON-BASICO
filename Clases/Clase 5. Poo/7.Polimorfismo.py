"""
El polimorfismo en la POO nos permite modificar el comportamiento 
de una clase padre para adaptarlo a las necesidades de una clase hija. 
Esto nos ayudará a crear una clase general con unas definiciones 
por defecto que luego podremos ir adaptando según las necesidades 
de la clase hija
"""
class Vehiculo:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def num_ruedas(self):
        pass

class Motocicleta(Vehiculo):
    def __init__(self):
        super().__init__('Motocicleta')

    def num_ruedas(self):
        return 2

moto = Motocicleta()
print(moto.num_ruedas())