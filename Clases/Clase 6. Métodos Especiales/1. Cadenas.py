#Métodos de las cadenas
#upper(): Devuelve la cadena con todos sus caracteres a mayúscula
cadena="Hola Mundo".upper()
print(cadena)
#lower(): Devuelve la cadena con todos sus caracteres a minúscula
cadena="Hola Mundo".lower()
print(cadena)
#capitalize(): Devuelve la cadena con su primer carácter en mayúscula
cadena="hola mundo".capitalize()
print(cadena)
#title(): Devuelve la cadena con el primer carácter de cada palabra en mayúscula
cadena="hola mundo".title()
print(cadena)
#count(): Devuelve una cuenta de las veces que aparece una subcadena en la cadena
cadena="Hola mundo".count('mundo')
print(cadena)
#find(): Devuelve el índice en el que aparece la subcadena (-1 si no aparece)
cadena="Hola mundo".find('mundo')
print(cadena)
cadena="Hola mundo".find('mundoz')
print(cadena)
#rfind(): Devuelve el índice en el que aparece la subcadena, empezando por el final
cadena="Hola mundo mundo mundo".rfind('mundo')
print(cadena)
#isdigit(): Devuelve True si la cadena es todo números (False en caso contrario)
c = "hola"
bandera=c.isdigit()
print(bandera)
#isalnum(): Devuelve True si la cadena es todo números o carácteres alfabéticos
c2 = "ABC10034po"
bandera=c2.isalnum()
print(bandera)
#isalpha(): Devuelve True si la cadena es todo carácteres alfabéticos
bandera=c2.isalpha()
print(bandera)
print("Holamundo".isalpha())
#islower(): Devuelve True si la cadena es todo minúsculas
bandera="hola mundo".islower()
print(bandera)
#isupper(): Devuelve True si la cadena es todo mayúsculas
"Hola mundo".isupper()
print("HOLA MUNDO".isupper())
#istitle(): Devuelve True si la primera letra de cada palabra es mayúscula
bandera="Hola Mundo".istitle()
print(bandera)
#isspace(): Devuelve True si la cadena es todo espacios
"  -  ".isspace()
print(" ".isspace())

#startswith(): Devuelve True si la cadena empieza con una subcadena
"Hola mundo".startswith("Mola")
print("Hola mundo".startswith("Hola"))
#endswith(): Devuelve True si la cadena acaba con una subcadena
"Hola mundo".endswith('mundo')
print("Hola mundo".endswith('Mundo'))
#split(): Separa la cadena en subcadenas a partir de sus espacios y devuelve una lista
lista="Hola mundo mundo".split()
print("Hola mundo mundo".split())
print(lista[0])
print(lista[1])
print(lista[2])
#Podemos indicar el carácter a partir del que se separa:
lista="Hola,mundo,mundo,otra,palabra".split(',')
print(lista)
print(lista[3])
#join(): Une todos los caracteres de una cadena utilizando un caracter de unión
cadena=",".join("Hola mundo")
print(cadena)
cadena=" ".join("Hola")
print(cadena)
#strip(): Borra todos los espacios por delante y detrás de una cadena y la devuelve
cadena="   Hola mundo     ".strip()
print(cadena)
#Podemos indicar el carácter a borrar:
cadena="-----Hola mundo---".strip('-')
print(cadena)
#replace(): Reemplaza una subcadena de una cadena por otra y la devuelve
cadena="Hola mundo".replace('o','0')
print(cadena)
#Podemos indicar un límite de veces a reemplazar:
cadena="Hola mundo mundo mundo mundo mundo".replace(' mundo','*',2)
print(cadena)