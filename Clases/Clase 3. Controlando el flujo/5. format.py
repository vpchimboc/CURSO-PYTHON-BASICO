"""
MÉTODO FORMAT()
Nos permite mostrar los valores contenidos en una variable y utilizarlos 
dentro de una cadena de caracteres, sustituyendo el nombre de una variable con un juego de {}
ubicandolas en la posición donde queremos que se muestre dichos valores

"""
#Alternativa 1
nombre = "Carlos"
edad = 22

print("Hola {} tienes {} años".format(nombre, edad))

#Alternativa 2

print("Hola {nombre} tienes {edad} años".format(nombre = "Carlos", edad = 22))

#Alternativa 3

print("Hola {1} tienes {0} años".format(edad, nombre))