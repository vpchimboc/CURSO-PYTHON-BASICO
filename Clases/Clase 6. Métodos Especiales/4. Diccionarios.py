"""
Los diccionarios son objetos que contienen una lista 
de parejas de elementos. De cada pareja un elemento es la clave, 
que no puede repetirse, y, el otro, un valor asociado.
"""
#Métodos de los diccionarios
colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }
colores['amarillo']

#get(): Busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto
colores.get('negro','no se encuentra')

'amarillo' in colores

#keys(): Genera una lista en clave de los registros del diccionario
colores.keys()

#values(): Genera una lista en valor de los registros del diccionario
colores.values()

#items(): Genera una lista en clave-valor de los registros del diccionario
colores.items()
for c in colores:
    print(colores[c])

for c,v in colores.items():
    print(c,v) # clave, valor

#pop(): Extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto
colores.pop("amarillo","no se ha encontrado")

colores

colores.pop("negro","no se ha encontrado")

colores

#clear(): Borra todos los registros de un diccionario
colores.clear()
colores