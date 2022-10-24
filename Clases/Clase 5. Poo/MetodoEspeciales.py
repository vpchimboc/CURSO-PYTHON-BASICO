class Coche:
    def __init__(self, marca,kilomentros, anio):
        self.marca=marca
        self.kilometros=kilomentros
        self.anio=anio
    def __del__(self):
        print(f"Se ha vendido el auto {self.marca}")
    def__arrancar__(self, arrancamos):
        self.enmarcha=arrancamos
        if(self.arran)
    def __str__(self):
        return "El auto tiene un {}, tiene {}, y es del anio {}".format(self.marca, self.kilometros, self.anio)


michoe=Coche("Audi", 200, 1995)
print(str(michoe))