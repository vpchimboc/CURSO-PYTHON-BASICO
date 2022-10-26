#Ficheros JSON

# Importar el módulo
import json
# Cadena de caracteres en el formato JSON
contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

datos = []

for nombre, empleo, email in contactos:
    datos.append({"nombre":nombre, "empleo":empleo, "email":email})
print(datos)
#Para escribir JSON en un archivo, llame al json.dumps() función.
with open("contactos.json", "w") as jsonfile:
    json.dump(datos, jsonfile)
datos = None
#Para leer un archivo JSON, simplemente puede llamar al json.loads() función.
with open("contactos.json", 'r') as jsonfile:
    datos = json.load(jsonfile)
    for contacto in datos:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])