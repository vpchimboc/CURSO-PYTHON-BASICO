"""
La encapsulación nos permite agrupar datos 
y controlar su comportamiento en nuestra clase. 
También nos permite controlar el acceso a nuestros 
datos y prevenir modificaciones no autorizadas.
"""
class Coche:
    #Constructor
    def __init__(self, marca,kilomentros, anio):
        self.__marca=marca #encapsulamos un atributo  es privado
        self._kilometros=kilomentros
        self.anio=anio
        print(f"Se ha creado un auto {self.__marca}, con {self._kilometros} kilometros")
    #Metodo get
    @property
    def kilometros(self):
        return f"El Kilometro es {self._kilometros}"
    @property
    def marca(self):
        return self.__marca
     #Metodo set
    @kilometros.setter
    def kilometros(self,kilometros):
      self._kilometros=kilometros
    @marca.setter
    def marca(self,marca):
        self.__marca=marca
    

    def arrancar(self, arrancamos):
        self.enmarcha=arrancamos
        if(self.enmarcha):
            print("El auto se encuentra encendido")
        else:
            print("El auto se encuentra apagado")
    # Metodo str permite retornar un mensaje 
    def __str__(self):
        return "El auto tiene un {}, tiene {}, y es del anio {}".format(self.__marca, self._kilometros, self.anio)


micoche=Coche("Audi", 200, 1995)
print(str(micoche))
print(micoche.arrancar(True))
##acceder a los metodos accesores
print(micoche.kilometros)
micoche.kilometros=400
micoche.anio=1991
print(micoche.anio)
print(str(micoche))
