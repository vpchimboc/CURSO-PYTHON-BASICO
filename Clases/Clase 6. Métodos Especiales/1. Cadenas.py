#Métodos de las cadenas
#upper(): Devuelve la cadena con todos sus caracteres a mayúscula
"Hola Mundo".upper()

#lower(): Devuelve la cadena con todos sus caracteres a minúscula
"Hola Mundo".lower()

#capitalize(): Devuelve la cadena con su primer carácter en mayúscula
"hola mundo".capitalize()

#title(): Devuelve la cadena con el primer carácter de cada palabra en mayúscula
"hola mundo".title()

#count(): Devuelve una cuenta de las veces que aparece una subcadena en la cadena
"Hola mundo".count('mundo')

#find(): Devuelve el índice en el que aparece la subcadena (-1 si no aparece)
"Hola mundo".find('mundo')

"Hola mundo".find('mundoz')

#rfind(): Devuelve el índice en el que aparece la subcadena, empezando por el final
"Hola mundo mundo mundo".rfind('mundo')

#isdigit(): Devuelve True si la cadena es todo números (False en caso contrario)
c = "100"
c.isdigit()

#isalnum(): Devuelve True si la cadena es todo números o carácteres alfabéticos
c2 = "ABC10034po"
c2.isalnum()

#isalpha(): Devuelve True si la cadena es todo carácteres alfabéticos
c2.isalpha()

"Holamundo".isalpha()

#islower(): Devuelve True si la cadena es todo minúsculas
"Hola mundo".islower()

#isupper(): Devuelve True si la cadena es todo mayúsculas
"Hola mundo".isupper()

#istitle(): Devuelve True si la primera letra de cada palabra es mayúscula
"Hola Mundo".istitle()

#isspace(): Devuelve True si la cadena es todo espacios
"  -  ".isspace()

#startswith(): Devuelve True si la cadena empieza con una subcadena
"Hola mundo".startswith("Mola")

#endswith(): Devuelve True si la cadena acaba con una subcadena
"Hola mundo".endswith('mundo')

#split(): Separa la cadena en subcadenas a partir de sus espacios y devuelve una lista
"Hola mundo mundo".split()[0]

#Podemos indicar el carácter a partir del que se separa:
"Hola,mundo,mundo,otra,palabra".split(',')

#join(): Une todos los caracteres de una cadena utilizando un caracter de unión
",".join("Hola mundo")

" ".join("Hola")

#strip(): Borra todos los espacios por delante y detrás de una cadena y la devuelve
"   Hola mundo     ".strip()

#Podemos indicar el carácter a borrar:
"-----Hola mundo---".strip('-')

#replace(): Reemplaza una subcadena de una cadena por otra y la devuelve
"Hola mundo".replace('o','0')

#Podemos indicar un límite de veces a reemplazar:
"Hola mundo mundo mundo mundo mundo".replace(' mundo','',4)
