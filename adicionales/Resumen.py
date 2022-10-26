print("Ficheros de texto")
#Crear fichero y escribir texto
texto = "(2,3),(5,5),(-3, -1),(0,0)"
fichero = open('puntos.txt','w')  # fichero.txt ruta donde lo crearemos, w indica modo de escritura, write (puntero principio)
fichero.write(texto) # escribimos el texto
fichero.close()  # cerramos el fichero

#Lectura de un fichero de texto
fichero = open('puntos.txt','r')  # modo lectura read, por defecto ya es r, no es necesario
texto = fichero.read() # lectura completa
fichero.close()
#imprimir texto
print(texto)
##############################################
#Con pickle
class Punto:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
import pickle
puntos=[Punto(2,3),Punto(5,5),Punto(-3, -1),Punto(0,0)]
#Escribir archivo
f = open('puntos.pckl','wb')
pickle.dump(puntos, f)
f.close()
#Leer archivo
f = open('puntos.pckl','rb')
puntos = pickle.load(f)
f.close()
for p in puntos:
    print(p)

########ARCHIVO CSV
#importamos el módulo csv
import csv
puntos = [
    (2,3),(5,5),(-3, -1),(0,0)
]
#Escribiendo a un Archivo CSV
#escribir datos a un archivo CSV usando la función csv.writer

with open("puntos.csv", "w", newline="\n") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for punto in puntos:
        writer.writerow(punto)

#Leyendo un Archivo CSV Con csv.reader

with open("puntos.csv", newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for x, y in reader:
        print(x, y)


############ARCHIVO JSON
#Ficheros JSON

# Importar el módulo
import json
# Cadena de caracteres en el formato JSON
puntos = [
    (2,3),(5,5),(-3, -1),(0,0)
]

datos = []

for x,y in puntos:
    datos.append({"x":x, "y":y})
print(datos)
#Para escribir JSON en un archivo, llame al json.dumps() función.
with open("puntos.json", "w") as jsonfile:
    json.dump(datos, jsonfile)
datos = None
#Para leer un archivo JSON, simplemente puede llamar al json.loads() función.
with open("puntos.json", 'r') as jsonfile:
    datos = json.load(jsonfile)
    for punto in datos:
        print(punto["x"], punto["y"])