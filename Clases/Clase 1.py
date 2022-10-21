#1. Declaración de variables
#Python puede identificar el tipo de dato que quiere almacenar
numero_uno=2
#Python puede diferenciar mayúsculas de minúsculas
Numero_uno="Hola mundo python"
print(numero_uno)
print(Numero_uno)
#Ejercicio 1
print("Esto es una suma")
numero_uno=2
numero_dos=4
resultado=numero_uno+numero_dos
print(resultado)
"""2. Manipulación de cadenas de caracteres
Operaciones
"""
print("2. Manipulación de cadenas de caracteres")
#Asignación.- Consiste en asignar una cadena de caracteres a otra. Para lo cual es necesario utilizar el operador +=
print("Asignación: ")
mensaje="Hola"
mensaje+=" "
mensaje+="Verónica"
print(mensaje)
#Concatenación.- Es una operación que consiste en unir dos cadenas o más, para formar una cadena de mayor tamaño. Para lo cual es necesario utilizar el operador +
print("Concatenación: ")
mensaje="Hola"
espacio=" "
nombre="Verónica"
print(mensaje+espacio+nombre)
#concatenación con numeros
resultado=str(resultado)
print("El resultado de la suma es: " + resultado)
#Búsqueda.- Consiste en localizar dentro de una cadena, una subcadena más pequeña a un carácter. Para lo cual es necesario utilizar el método find.
print("Búsqueda")
mensaje="Hola Verónica"
buscar_subcadena=mensaje.find("Verónica")
print(buscar_subcadena)
#La extracción.- se trata de sacar fuera e una cadena, una porción de la misma según su posición dentro de ella. Para ello es necesario indicar la posición a extraer [1:8]
print("extracción")
mensaje="Hola Veronica"
extraer_subcadena=mensaje[5:9]
print(extraer_subcadena)
#La comparación.- se utiliza para comparar dos cadenas de caracteres. Para ello se utiliza el operador ==
print("comparación")
mensaje_uno="Hola"
mensaje_dos="Hola"
print(mensaje_uno==mensaje_dos)
"""3. Palabras reservadas
Las palabras reservadas, son identificadores para uso exclusivo del lenguaje de programaci[on, que no pueden ser utilizadas para identificar y nombrar variables, metodos, objetos o cualquier elemento dentro de nuestro codigo
Existen 28 palabras reservadas
and     del     for         is      raise   assert
if      else    elif        from    lambda  return
break   global  not         try     class   except
or      while   continue    exec    import  yield
def     finally in          print
"""
print("3. Palabras reservadas")
prinT=5
Print=6
resultado=prinT+Print
print(str(resultado))
"""4. Operadores aritméticos
Son aquellos que manipulan datos numéricos, tanto numéricos enteros, asi como decimales también conocidos como reales
suma (+)
rest (-)
multipliciones(*)
divisiones(/)
modulo o residuo(%) 
exponenciales(**)
División entera(//)
"""
print("4. Operaciones Aritméticas: ")
print("Suma: ")
numero_uno=5
numero_dos=4
resultado=numero_uno + numero_dos
print("El resultado de la suma: "+str(resultado))
print("Resta: ")
numero_uno=5
numero_dos=4
resultado=numero_uno - numero_dos
print("El resultado de la resta: "+str(resultado))
print("Multiplicación: ")
numero_uno=5
numero_dos=4
resultado=numero_uno * numero_dos
print("El resultado de la multiplicación: "+str(resultado))
print("Exponente o potencia: ")
numero_uno=2
exponente=5
resultado=numero_uno ** exponente
print("El resultado del exponente y potencia: "+str(resultado))
print("División: ")
numero_uno=4
numero_dos=2
resultado=numero_uno / numero_dos
print("El resultado de la división: "+str(resultado))
print("Modulo o Residuo: ")
numero_uno=30
numero_dos=8
resultado=numero_uno % numero_dos
print("El resultado de la modulo o residuio: "+str(resultado))
print("Divisón entera: ")
numero_uno=4
numero_dos=2
resultado=numero_uno // numero_dos
print("El resultado de la división entera: "+str(resultado))
"""5. Comentarios 
Son anotaciones legibles del programador en el código fuente del programa.
En Python, la forma de añadir comentarios son los siguientes
- Con el signo # para linea de código
- comillas dobless sin asignación""
- comillas triples """ """
"""
#Esto es un comentario
"Esto es un comentario"
"""Esto es un comentario multilinea"""
"""6. Tipos de Datos en Python
1. Enteros y Largos -: int y long
2. Flotantes-: float
3. Números complejos-: complex
4. Cadenas-: str
5. Booleanos-: bool
"""
print("6. Tipos de Datos")
"Tipo de Dato Enteros y Largo"
numero=15
print(numero,type(numero))
"Tipo de Dato Flotante"
numero_flotante=15.5
print(numero_flotante,type(numero_flotante))
"Tipo de Dato Complejo"
numero_complejo=5+6j
print(numero_complejo,type(numero_complejo))
"Tipo de Dato String"
nombre="Veronica"
print(nombre,type(nombre))
"Tipo de Dato Booleana"
verdadero_falso=3==3
print(verdadero_falso,type(verdadero_falso))
"""7. Entrada de datos desde teclado
Permite que el usuario pueda interactuar con el programa
"""
print("Entrada de datos")

palabra=input("Intoduce una palabra: ")
num_int=int(input("Introduce un número entero: "))
num_float=float(input("Introduce un número flotante: "))
num_complejo=complex(input("Introduce un número complejo: "))

print("String: ", palabra)
print("Entero: ", num_int)
print("Flotante: ", num_float)
print("Complejo: ", num_complejo)

#Ejercicio
nombre=input("Cual es tu nombre: ")
print("Hola "+nombre + ", vamos a realizar una suma.")
num_uno=int(input("Por favor introduce el primer valor: "))
num_dos=int(input("Por favor introduce el segundo valor: "))
resultado=num_uno+num_dos
print(nombre+" el resultado de la suma es: ", resultado)

"""8. Sentencias Condicionales
Es una instrucción o grupo de instrucciones, que se ejecuta cuando a un programa se le establece una condición lógica.
Al cumplirse dicha condición, el programa ejecuta la instrucción que ha sido asignada a esta condición
Sentencias condicionales simples
if Condicion lógica:
   Instrucción

"""
num_uno=5
if num_uno==10:
    print("El numero es cinco")
print("Fin.")