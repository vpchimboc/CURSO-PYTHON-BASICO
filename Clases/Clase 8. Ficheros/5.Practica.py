print("Práctica")
print("Catálogo de pelí­culas con ficheros y pickle")
from io import open
import pickle

class Pelicula:
    
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la pelí­cula:',self.titulo)
        
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:
    
    peliculas = []
    
    # Constructor de clase
    def __init__(self):
        self.cargar()
        
    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar()
        
    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catálogo está vacío")
            return
        for p in self.peliculas:
            print(p)
            
    def cargar(self):
        fichero = open('catalogo.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            del(fichero)
            print("Se han cargado {} peli­culas".format( len(self.peliculas) ))
    
    def guardar(self):
        fichero = open('catalogo.pckl', 'wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()
        del(fichero)
    
   
#Creando un objeto catálogo
c = Catalogo()
c.mostrar()
c.agregar( Pelicula("El Padrino", 175, 1972) )
c.agregar( Pelicula("El Padrino: Parte 2", 202, 1974) )
c.mostrar()

#Recuperando el catálogo al crearlo de nuevo
c = Catalogo()

c.mostrar()



c = Catalogo()

c.agregar( Pelicula("Prueba", 100, 2005) )

c.mostrar()



c = Catalogo()

c.mostrar()