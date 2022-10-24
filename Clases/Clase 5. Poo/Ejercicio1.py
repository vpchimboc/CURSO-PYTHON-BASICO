"""
Bienvenido a la actividad llamada “Impuestos”, en esta ocasión se brindará un ejercicio práctico para que logres aplicar los conceptos vistos en la clase sobre programación orientada a objetos.
Objetivos
Crear clases y objetos 
Utilizar los constructores
Utilizar la herencia
Descripción del problema
Los asesores en los bancos se enfrentan a una pregunta común de parte de los ciudadanos: ¿Debo pagar impuestos por tener dinero en el banco? Muy bien, el día de hoy vamos a escribir un programa para dar respuesta a esta inquietud.
Implementa un programa con una clase llamada Persona que contenga dos atributos que serán ingresados por teclado: nombre y edad. Además, que contenga un método llamado imprimir que devuelva el nombre y la edad.
Después, crea otra clase llamada Ciudadano que herede de la clase Persona y agregue un atributo llamado depósito que será ingresado por teclado. Además, contendrá el método llamado imprimir para mostrar el depósito. 
Así mismo, crea otro método llamado impuestos y si el depósito es superior a 4000 USD muestre que SI debe pagar, caso contrario no deberá pagar. 
Los datos para este ejercicio son los siguientes: 

Nombre Edad Depósito
Manuel Chima 25 6700
Fayle García 56 3500
Lesly Rodríguez 34  9000
Mario Herrera  45 2500


Instrucciones
Observa el siguiente instructivo, donde se explicara el porqué, el cómo y el paso a paso de cada línea de código que escribirás:
"""
 #1. Ingrese a Visual Studio Code y en la carpeta “Actividades” cree un nuevo archivo con el nombre “actividad_poo.py”.

 #2. Cree la clase llamada Persona con su constructor y los dos atributos: nombre y edad, recuerde que serán ingresados por teclado. Además, defina el método para imprimir el nombre y la edad.

class Persona:
    nombre=""
    


 #3. Crea la clase Ciudadano y entre paréntesis pase el nombre de la clase de la cual hereda. Dentro de la clase defina el constructor, use la función super().__init__() para heredar los atributos de la clase Persona y debajo coloque el atributo depósito que será ingresado por teclado. 



 #4. Define el método imprimir para obtener el depósito del usuario, pero como necesitamos el nombre y edad que vienen de la clase padre debemos colocar la función super().imprimir() 



 #5. Define el método de impuestos para devolver si el usuario debe o no pagar impuestos. 



#6. Cree el objeto con el nombre ciudadano1 y llame a los métodos imprimir e impuestos. 



 

#7. Realice un comentario multilínea dentro del programa e indique si los ciudadanos: Manuel, Fayle, Lesly y Mario deben pagar impuestos. 
