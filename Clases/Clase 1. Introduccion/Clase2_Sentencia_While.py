"""Iteraciones
Iterar significa realizar una acción varias veces. Cada vez que se repite se denomina iteración.

Sentencia While (Mientras)
Se basa en repetir un bloque a partir de evaluar una condición lógica, siempre que ésta sea True.

Queda en las manos del programador decidir el momento en que la condición cambie a False para hacer que el While finalice.
"""
c = 0
while c <= 5:
    c+=1
    print("c vale",c)

"""
Sentencia Else en bucle While
Se encadena al While para ejecutar un bloque de código una vez la condición ya no devuelve True (normalmente al final).
"""

c = 0
while c <= 5:
    c+=1
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale",c)

"""
Instrucción Break
Sirve para "romper" la ejecución del While en cualquier momento. No se ejecutará el Else, ya que éste sólo se llama al finalizar la iteración.
"""
c = 0
while c <= 5:
    c+=1
    if (c==4):
        print("Rompemos el bucle cuando c vale",c)
        break
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale",c)

"""
Instrucción Continue
Sirve para "saltarse" la iteración actual sin romper el bucle.
"""

c = 0
while c <= 5:
    c+=1
    if c==3 or c==4:
        print("Continuamos con la siguiente iteración",c)
        continue
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale",c)

#Creando un menú interactivo
print("Bienvenido al menú interactivo")
while(True):
    print("""¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir""")
    opcion = input()
    if opcion == '1':
        print("Hola, espero que te lo estés pasando bien")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ",n1+n2)
    elif opcion =='3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
