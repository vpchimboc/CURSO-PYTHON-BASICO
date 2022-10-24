print("Sistema para calcular el promedio de un alumno.")

nombre = input("Para comenzar, ¿Cuál es tu nombre?: ")

matematicas = float(input(nombre + " ¿Cuál es tu calificación en matemáticas?: "))
quimica = float(input(nombre + " ¿Cuál es tu calificación en química?: "))
biologia = float(input(nombre + " ¿Cuál es tu calificación en biología?: "))

promedio = (matematicas + quimica + biologia) / 3

if promedio >= 6:
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', promedio)
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', round(promedio,2))
else:
    print("Lo sentimos " + nombre + " has 'reprobado' con un promedio de: ", promedio)
    print("Lo sentimos " + nombre + " has 'reprobado' con un promedio de: ", round(promedio,1))

print("Fin.")
