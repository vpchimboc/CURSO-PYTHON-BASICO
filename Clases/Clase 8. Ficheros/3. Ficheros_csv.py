print("adicionales/Ficheros CSV")
"""
Valores separados por comas (comma-separated values)
Documentación: https://code.tutsplus.com/es/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907
"""

#importamos el módulo csv
import csv
contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]
#Escribiendo a un Archivo CSV
#escribir datos a un archivo CSV usando la función csv.writer
"""
La función writer() creará un objeto apto para escritura. 
Para iterar los datos sobre las filas, necesitaremos usar 
la función writerows().
"""
with open("adicionales/contactos.csv", "w", newline="\n") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for contacto in contactos:
        writer.writerow(contacto)

#Leyendo un Archivo CSV Con csv.reader
"""
abrimos nuestro archivo CSV como File. 
Entonces definimos el objeto lector y 
usamos el método csv.reader para extraer los datos 
al objeto. Entonces iteramos sobre el objeto reader 
y recuperamos cada fila de nuestros datos.
"""
with open("contactos.csv", newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for nombre, empleo, email in reader:
        print(nombre, empleo, email)

#Escribiendo a un Archivo CSV Usando DictWriter

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]
"""
Primero definimos los fieldnames, los cuales representarán 
los encabezados de cada columna en el archivo CSV. 
El método writerrow() escribirá a una fila a la vez. 
Si quieres escribir todos los datos de una vez, 
usarás el método writerrows().
"""
with open("contactos2.csv", "w", newline="\n") as csvfile:
    campos = ["nombre", "empleo", "email"]
    writer = csv.DictWriter(csvfile, fieldnames=campos)
    writer.writeheader()
    for nombre, empleo, email in contactos:
        writer.writerow({
            "nombre": nombre, "empleo": empleo, "email": email 
        })
#Leyendo un Archivo CSV Con DictReader
"""DictWriter nos permite leer un archivo CSV 
mapeando datos a un diccionario en vez de cadenas 
como en el caso del módulo csv.rader. Aunque el fieldname 
es un parámetro opcional, es importante siempre 
tener etiquetadas tus columnas para legibilidad."""     

with open("contactos2.csv", newline="\n") as csvfile:
    reader = csv.DictReader(csvfile)
    for contacto in reader:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])