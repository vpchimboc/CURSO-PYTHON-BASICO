"""
POO.- Paradigma de la Programación
Modelo de diseño y desarrollo de Programa
- Objeto.- Es todo lo que nos rodea, que tienen caracteristicas y métodos
- Clase .- Es una plantilla de un objeto
"""
#Como crear una clase
#La primera letra debe de ser en Mayusculas
class Gelatina:
      #Esta clse define el estado y el comportamiento de una Gelatina
    #Atributos de clase
    nombre="" 
    #constructor
    def __init__(self,sabor, color,tamanio):
    #atrubutos de instancia
      self.sabor=sabor
      self.color=color
      self.tamanio=tamanio
    #métodos
    def imprimir(self):
        print(f"La gelatina es de {self.sabor}") 
        print(f"La gelatina se ve de {self.color}")
        print(f"La gelatina es de {self.tamanio}")  

gel=Gelatina("Frutilla","Rojo","Grande")
gel1=Gelatina("Pomelo","Naranja","Mediana")
print("Objeto 1")
gel.imprimir()
print("Objeto 2")
gel1.imprimir()
