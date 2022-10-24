class Persona:
    def __init__(self, nombre, edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    def datosPersonales(self):
        print(f"El nombre de la persona es: {self.nombre}")
        print(f"La edad de la persona es: {self.edad}")
        print(f"El sexo de la persona es: {self.sexo}")
persona1=Persona("Verónica",31,"Femenino")
persona2=Persona("Diego",33,"Masculino")
persona3=Persona("Paulina",35,"Masculino")
persona1.datosPersonales()
persona2.datosPersonales()
persona3.datosPersonales()

