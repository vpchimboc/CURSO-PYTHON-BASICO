"""
La clase range Genera secuencias de números inmutables, es decirs, 
que no se pueden modificar, estas secuencias se generan a partir de un rango previamente establecido
se utiliza en los ciclos y bucles
sintaxis
range(start,stop,step )
start.- indica el número a partir del cual se comenzará a generar la secuencia de números, y este número siempre formará parte de la secuencia.
stop.- valor entero, que indica el número hasta el cual se va a generar la secuencia de números, y este jamás formará parte de la secuencia
step.- Es un valor entero, que indica el incremento o decremento de la sucesión numérica entre un número y el siguiente
"""
print(list(range(10)))
print(list(range(2,10)))
print(list(range(2,10,2)))
print(list(range(0,10,3)))

