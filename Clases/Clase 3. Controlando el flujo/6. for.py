"""
El ciclo o buche for, es una estructura de control que nos permite repetir
un bloque de instrucciones (sentencias)
sintaxis
for variable in objeto_iterable:
    instrucciones

Un objeto iterable, es aquel que permite recorrer sus elementos uno a uno
Como por ejemplo, una cadena de caracteres.

"""
cadena="Hola"
for variable in cadena:
    print(variable)
print("Fin del programa")

#Ejercicio 
"""
Desarrollar un programa que invierta una cadena de caracteres,
y a su vez, esta cadena de caracteres deberá ser ingresada por el
usuario desde teclado
Requerimientos indispensables
- No se permite modificar la cadena de caracteres original.
- Utilizar el ciclo o bucle for.
"""
"""
cadena=input("Ingrese un cadena de caracteres: ")

cont =1
for elemento in cadena:
    
    reversed_language = cadena[::-1]
    
    print(reversed_language)
    if cont==1:
        break

"""
"""
cadena=input("Ingrese la cadena: " )
i=len(cadena)
for caracter in cadena:
    print(cadena[i-1],end=" ")
    i=i-1
    
cadena=input("Ingrese la cadena: ")
for elemento in reversed(cadena) :
    print(elemento, end=" ")

"""
"""
cadena=input("Ingrese la cadena: " )
salida=""
for caracter in cadena:
    salida=caracter+salida
print(salida)
"""
cadena =input ('Ingrese una cadena de cacteres')
longitud= len (cadena)
p=''
for j in cadena:
    p=j+p
print(p)
