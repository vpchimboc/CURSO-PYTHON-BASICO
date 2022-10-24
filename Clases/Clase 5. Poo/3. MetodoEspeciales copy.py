class Coche:
    #Constructor
    def __init__(self, marca,kilomentros, anio):
        self.marca=marca
        self.kilometros=kilomentros
        self.anio=anio
        print(f"Se ha creado un auto {self.marca}, con {self.kilometros} kilometros")
    
    #Elimina un objeto
    def __del__(self):
        print(f"Se ha vendido el auto  marca {self.marca}")
    # Metodo str permite retornar un mensaje 
    def __str__(self):
        return "El auto tiene un {}, tiene {}, y es del anio {}".format(self.marca, self.kilometros, self.anio)


michoe=Coche("Audi", 200, 1995)
print(str(michoe))
del(michoe)
print(str(michoe))