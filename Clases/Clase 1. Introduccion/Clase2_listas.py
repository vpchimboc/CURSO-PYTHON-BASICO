"""
Las listas
Tipo compuesto de dato que puede almacenar distintos valores (llamados ítems) ordenados entre [ ] y separados con comas.
"""
numeros = [1,2,3,4]
datos = [4,"Una cadena",-15,3.14,"Otra cadena"]

"""
Índices y slicing (Cortar cadenas)
Funcionan de una forma muy similar a las cadenas de caracteres.
"""
datos[0]
datos[-1]
datos[-2:]
print(datos[-2:])
"""
Suma de listas
Da como resultado una nueva lista que incluye todos los ítems.
"""
numeros + [5,6,7,8]

"""
Son modificables
A diferencia de las cadenas, en las listas sí podemos modificar sus ítems utilizando índices:
"""
pares = [0,2,4,5,8,10]
pares[3]= 6

#Integran funcionalidades internas, como el método .append() para añadir un ítem al final de la lista
pares.append(12)
pares.append(7*2)

#Y una peculiaridad, es que también aceptan asignación con slicing para modificar varios ítems en conjunto
letras = ['a','b','c','d','e','f']
letras[:3]
letras[:3] = ['A','B','C']
print(letras)

#La función len() también funciona con las listas del mismo modo que en las cadenas:
len(letras)
len(pares)

#Listas dentro de listas (anidadas)
#Podemos manipular fácilmente este tipo de estructuras utilizando múltiples índices, como si nos refieréramos a las filas y columnas de una tabla.
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]
print(r)
r[0]  # Primera sublista
r[-1]  # Última sublista
r[0][0]  # Primera sublista, y de ella, primer ítem
r[1][1]  # Segunda sublista, y de ella, segundo ítem
r[2][2]  # Tercera sublista, y de ella, tercer ítem
r[-1][-1]  # Última sublista, y de ella, último ítem