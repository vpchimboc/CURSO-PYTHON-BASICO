"""
POO
- Clase
- Instancia
- Variable de clase
- Variable de instancia
- Metodo
- Objeto
"""
class Gelatina:
    def __init__(self,sabor, color,tamanio):
      self.sabor=sabor
      self.color=color
      self.tamanio=tamanio
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

gels=[gel,gel1]
print(gels[0].imprimir())