"""
La herencia nos permite generar una jerarquía de clases 
en las que podemos compartir funcionamientos comunes y 
en el que existirá una clase padre también conocida como superclase
 y una o varias clases hijas conocidas como subclases.
"""
class Persona:
    def __init__(self, nombre, edad, apellido, sexo):
        self.nombre=nombre
        self.edad=edad
        self.apellido=apellido
        self.sexo=sexo
    def datosPersonales(self):
        print(f"El nombre de la persona es: {self.nombre}")
        print(f"El apellido de la persona es: {self.apellido}")
        print(f"La edad de la persona es: {self.edad}")
        print(f"El sexo de la persona es: {self.sexo}")

miPersona=Persona("Veronica",31,"Chimbo","Femenino")
miPersona.datosPersonales()
print("##############")
#Herencia
class Empleado(Persona):
    def __init__(self, nombre, edad, apellido, sexo, departamento):
        super().__init__(nombre, edad, apellido, sexo)
        self.departamento=departamento

    def datosEmpleado(self,vacaciones,salario):
        super().datosPersonales()
        print(f"El Departamento al cual pertenece es: {self.departamento}")
        print(f"Sus días de vacaciones son: {vacaciones}")
        print(f"Su salario es: {salario}")

miEmpleado=Empleado("Paulina",31,"Coronel","Femenino","Sistemas")
#miEmpleado.datosPersonales()
miEmpleado.datosEmpleado(30,250)
