print("Ficheros de texto")
#Crear fichero y escribir texto
texto = "Una línea con texto\nOtra línea con texto"
fichero = open('fichero.txt','w')  # fichero.txt ruta donde lo crearemos, w indica modo de escritura, write (puntero principio)
fichero.write(texto) # escribimos el texto
fichero.close()  # cerramos el fichero

#Lectura de un fichero de texto
fichero = open('fichero.txt','r')  # modo lectura read, por defecto ya es r, no es necesario
texto = fichero.read() # lectura completa
fichero.close()
#imprimir texto

fichero = open('fichero.txt','r')
texto = fichero.readlines() # leer creando una lista de líneas
fichero.close()
#imprimir texto

#Extensión de un fichero de texto
fichero = open('fichero.txt','a')  # modo a, append, añadir - extender (puntero al final)
fichero.write('\nOtra línea más abajo del todo')
fichero.close()
#Lectura de un fichero no existente
#fichero = open('fichero_inventado.txt','r')
fichero = open('fichero_inventado.txt','a+')  # Extensión con escritura simultánea, crea fichero si no existe

#Lectura línea a línea
print("Lectura línea a línea")
fichero = open('fichero.txt','r')
fichero.readline()   # Línea a línea
fichero.readline()
fichero.readline()
fichero.close()
#Lectura línea a línea secuencial
with open("fichero.txt", "r") as fichero:
    for linea in fichero:
        print(linea)
#Manejando el puntero
fichero = open('fichero.txt','r')
fichero.seek(0) # Puntero al principio
fichero.read(10) # Leemos 10 carácteres
fichero.read(10) # Leemos 10 carácteres más, a partir del 10 donde está el puntero
fichero.seek(0)
fichero.seek(len(fichero.readline())) # Leemos la primera línea y situamos el puntero al principio de la segunda
fichero.read() # Leemos todo lo que queda del puntero hasta el final

#Lectura y escritura a la vez
fichero2 = open('fichero2.txt','w')
texto = "Línea 1\nLínea 2\nLínea 3\nLínea 4"
fichero2.write(texto)

fichero2.close()
fichero2 = open('fichero2.txt','r+')  # + escritura simultánea, puntero al principio por defecto
fichero2.write('asdfgh')

fichero2.close()
#Modificar una línea específica
fichero2 = open('fichero2.txt','r+')  # modo lectura con escritura, puntero al principio por defecto
texto = fichero2.readlines() # leemos todas las líneas
texto[2] = "Esta es la línea 3 modificada\n"  # indice menos 1
texto

fichero2.seek(0) # Ponemos el puntero al principio
fichero2.writelines(texto)
fichero2.close()