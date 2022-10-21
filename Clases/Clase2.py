"""
8. Sentencias condicionales compuestas
Son aquellas que nos permiten tener una instrucción a ejecutar de acuerdo a la condición establecida
if Condición lógica:
    Instrucción
else:
    Instrucción

"""
print("Sistema para calcular el promedio de un alumno")
nombre=input("Para comenzar, Cuál es tu nombre: ")
matematicas_discretas=float(input(nombre+ " Cuál es tu calificación en Matemáticas Discretas: "))
introduccion=float(input(nombre+ " Cuál es tu calificación en Introducción al desarrollo de Software: "))
ingles=float(input(nombre+ " Cuál es tu calificación en Inglés: "))

promedio=(matematicas_discretas+introduccion+ingles)/3
if promedio >= 7:
    print("Felicidades "+ nombre + " 'Aprobaste' con un promedio de: ", promedio)
    print("Felicidades "+ nombre + " 'Aprobaste' con un promedio de: ", round(promedio,2))
else:
    print("Lo sentimos "+ nombre + " Has 'Reprobado' con un promedio de: ", promedio)
    print("Lo sentimos "+ nombre + " Has 'Reprobado' con un promedio de: ", round(promedio,2))
print("Fin.")

"""
9. Sentencias condicionales múltiples
Son aquellas que nos permiten tener una instrucción a ejecutar de acuerdo a la condición establecida
if Condición lógica:
    Instrucción
elif Condición lógica:
    Instrucción
else:
    Instrucción

"""
print("=================================================")
print("CONVERTIDOR DE LETRAS")
print("=================================================")
numero=int(input("Cual es el número que deseas convertir: "))
if numero==1:
    print("El número es 'Uno'")
elif numero==2:
    print("El número es 'Dos'")
elif numero==3:
    print("El número es 'Tres'")   
elif numero==4:
    print("El número es 'Cuatro'")   
elif numero==5:
    print("El número es 'Cinco'") 
else:
    print("Este programa solo puede convertir hasta el número 5") 
print("Fin.") 

"""
10. Sentencias condicionales anidadas
Es una condición dentro de otra condición
if Condición lógica:
    Instrucción
elif Condición lógica:
    Instrucción
else:
    Instrucción

"""
print("=================================================\n")
print("CONVERSOR")
print("=================================================")
print("MENÚ DE OPCIONES\n")
print("Presiona 1 para convertir el número a palabra.")
print("Presiona 2 para convertir la palabra a número.")
menu=int(input("Cuál es tu opción deseada: "))
if menu==1:
    print("\nConversor de número a palabra\n")
    numero=int(input("Cual es el número que deseas convertir a palabra: "))
    numero=numero.lower()
    if numero==1:
        print("El número es 'Uno'")
    elif numero==2:
        print("El número es 'Dos'")
    elif numero==3:
        print("El número es 'Tres'")   
    elif numero==4:
        print("El número es 'Cuatro'")   
    elif numero==5:
        print("El número es 'Cinco'") 
    else:
        print("Este programa solo puede convertir hasta el número 5")
elif menu==2:
    print("\nConversor de palabra a numero\n")
    numero=input("Cual es el palabra que deseas convertir a numero: ")
    if numero=="uno":
        print("El número es '1'")
    elif numero=="dos":
        print("El número es '2'")
    elif numero=="tres":
        print("El número es '3'")   
    elif numero=="cuatro":
        print("El número es '4'")   
    elif numero=="cinco":
        print("El número es '5'") 
    else:
        print("Este programa solo puede convertir hasta el número 5")
else:
    print("Opción no disponible")
print("Fin")


    
  
  