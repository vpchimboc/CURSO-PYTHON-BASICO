"""
Parámetro end
Se utiliza para agregar cualquier cadena de caracteres al fina de la salida e impresión en pantalla de la función print()
End evita que la función print de un salto de línea
"""
print("Esto es un")
print("Ejemplo")

print("Esto es un", end="--")
print("Ejemplo")

"""
Parámetro sep
Ayudar a dar formato a las cadenas de caracteres
que deben imprimirse en pantalla, agregando un separador entre cadenas que se imprimirán
"""
print("1","2","3","4","5",sep=("--"))
