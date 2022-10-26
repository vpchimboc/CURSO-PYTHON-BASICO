#
#Lectura de un fichero de texto
fichero = open('puntos.txt','r')  # modo lectura read, por defecto ya es r, no es necesario
texto = fichero.read() # lectura completa
fichero.close()
#imprimir texto
print(texto)