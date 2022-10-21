print("Sistema para calcular el promedio de un alumno")
nombre=input("Para comenzar, Cuál es tu nombre: ")
matematicas_discretas=float(input(nombre+ " Cuál es tu calificación en Matemáticas Discretas: "))
introduccion=float(input(nombre+ " Cuál es tu calificación en Introducción al desarrollo de Software: "))
ingles=float(input(nombre+ " Cuál es tu calificación en Inglés: "))

promedio=(matematicas_discretas+introduccion+ingles)/3
if promedio >= 7:
    print("Felicidades "+ nombre + " 'Aprobaste' con un promedio de: ", promedio)
print("Fin.")

