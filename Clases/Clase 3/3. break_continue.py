"""
Para lograr la interrupción de una iteración, contamos con las sentencias break y continue
Break para detener la ejecución de una iteracción y salir de ella

"""
#Ejemplo para break

print("while con la sentencia break \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        break

    print("Valor actual de la variable: ", contador)

print("Fin del prgrama, la sentencia break se ha ejecutado.")
"""
Sentencia continue
Permite determinar la iteracción actual y volver al principio
"""
#Ejemplo para continue

print("\nwhile con la sentencia continue \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        continue

    print("Valor actual de la variable: ", contador)