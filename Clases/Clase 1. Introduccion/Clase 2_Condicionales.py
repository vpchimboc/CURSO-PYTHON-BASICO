"""Condiciones
Sentencia If (Si)
Permite dividir el flujo de un programa en diferentes caminos. El if se ejecuta siempre que la expresión que comprueba devuelva True
"""
print("########################")
print("       Condicionales   ")
print("########################")
print("########################")
print("       Sentencia If (Si)  ")
print("######################## \n")
if True:  # equivale a if not False
    print("Se cumple la condición")
    print("También se muestre este print")
#Podemos encadenas diferentes If
print("########################")
print("       IF anidados  ")
print("######################## \n")
a = 5
if a == 2:
    print("a vale 2")
if a == 5:
    print("a vale 5")
#O también anidar If dentro de If
print("########################")
print("       Anidar If dentro de If  ")
print("######################## \n")
a = 5
b = 10
if a == 5:
    print("a vale",a)
    if b == 10:
        print("y b vale",b)
#Como condición podemos evaluar múltiples expresiones, siempre que éstas devuelvan True o False
print("##################################")
print(" evaluar múltiples expresiones ")
print("################################## \n")
if a==5 and b == 10:
    print("a vale 5 y b vale 10")
#Sentencia Else (Sino)
#Se encadena a un If para comprobar el caso contrario (en el que no se cumple la condición).
print("########################")
print(" Sentencia Else (Sino) ")
print("######################## \n")
n = 11
if n % 2 == 0:
    print(n,"es un número par")
else:
    print(n,"es un número impar")
#Sentencia Elif (Sino Si)
#Se encadena a un if u otro elif para comprobar múltiples condiciones, siempre que las anteriores no se ejecuten.
print("########################")
print(" Encadena a un if u otro elif ")
print("######################## \n")

comando = "OTRA COSA"
if comando == "ENTRAR":
    print("Bienvenido al sistema")
elif comando == "SALUDAR":
    print("Hola, espero que te lo estés pasando bien aprendiendo Python")
elif comando == "SALIR":
    print("Saliendo del sistema...")
else:
    print("Este comando no se reconoce")
#Ejercicio 1
print("########################")
print(" Ejercicio 1 ")
print("######################## \n")

nota = float(input("Introduce una nota: "))
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Insuficiente")
#Es posible simular el funcionamiento de elif con if utilizando expresiones condicionales
nota = float(input("Introduce una nota: "))
if nota >= 9:
    print("Sobresaliente")
if nota >= 7 and nota < 9:
    print("Notable")
if nota >= 6 and nota < 7:
    print("Bien")
if nota >= 5 and nota < 6:
    print("Suficiente")
if nota < 5:
    print("Insuficiente")
#Instrucción Pass
#Sirve para finalizar un bloque, se puede utilizar en un bloque vacío.
if True:
    pass