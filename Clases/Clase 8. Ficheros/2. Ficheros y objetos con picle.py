print("El módulo pickle")
#Guardar estructura en fichero binario
import pickle
lista = [1,2,3,4,5] # Podemos guardar lo que queramos, listas, diccionarios, tuplas...
fichero = open('lista.pckl','wb') # Escritura en modo binario, vacía el fichero si existe
pickle.dump(lista, fichero) # Escribe la estructura en el fichero 
fichero.close()
#Recuperar estructura de fichero binario
fichero = open('lista.pckl','rb') # Lectura en modo binario
lista_fichero = pickle.load(fichero)
print(lista_fichero)

#Ejercicio 1
"""Lógica para trabajar con objetos
- Crear una colección
- Introducir los objetos en la colección
- Guardar la colección haciendo un dump
- Recuperar la colección haciendo un load
- Seguir trabajando con nuestros objetos
"""
class Persona:
    
    def __init__(self,nombre):
        self.nombre = nombre
        
    def __str__(self):
        return self.nombre
    

nombres = ["Héctor","Mario","Marta"]
personas = []

for n in nombres:
    p = Persona(n)
    personas.append(p)
    
import pickle
#Escribir archivo
f = open('personas.pckl','wb')
pickle.dump(personas, f)
f.close()
#Leer archivo
f = open('personas.pckl','rb')
personas = pickle.load(f)
f.close()
for p in personas:
    print(p)
