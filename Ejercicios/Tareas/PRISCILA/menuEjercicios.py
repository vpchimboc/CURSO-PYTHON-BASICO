def pedirOpcion():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

def diaVacaciones():
    # Ejercicios con Condicionales - Priscila Bernal
    print("SISTEMA DE CALCULO DE VACACIONES \n")
    nombre = input("Porfavor ingrese su nombre: ")
    clave = input("Porfavor ingrese la clave de su departamento (clave 1, clave 2 o clave 3): ")
    antiguedad = int(input("Porfavor ingrese sus años de antiguedad: "))
    if clave=="clave 1":
        if antiguedad==1:
            print("El trabajador " + nombre + " tiene derecho a 6 días de vacaciones") 
        elif antiguedad>=2 and antiguedad<=6:
            print("El trabajador " + nombre + " tiene derecho a 14 días de vacaciones") 
        elif antiguedad>=7:
            print("El trabajador " + nombre + " tiene derecho a 20 días de vacaciones") 
    elif clave=="clave 2":
        if antiguedad==1:
            print("El trabajador " + nombre + " tiene derecho a 7 días de vacaciones") 
        elif antiguedad>=2 and antiguedad<=6:
            print("El trabajador " + nombre + " tiene derecho a 15 días de vacaciones") 
        elif antiguedad>=7:
            print("El trabajador " + nombre + " tiene derecho a 22 días de vacaciones")  
    elif clave=="clave 3":
        if antiguedad==1:
            print("El trabajador " + nombre + " tiene derecho a 7 días de vacaciones") 
        elif antiguedad>=2 and antiguedad<=6:
            print("El trabajador " + nombre + " tiene derecho a 20 días de vacaciones") 
        elif antiguedad>=7:
            print("El trabajador " + nombre + " tiene derecho a 30 días de vacaciones")          
    print('fin')

def operacionNumeros():
    #Actividad con bucles -- Priscila Bernal
    opc=0
    sal=False
    while not sal:
        print("MENU DE OPERACIONES CON DOS NUMEROS")
        print("Opcion 1: Mostrar la suma de los dos numeros")
        print("Opcion 2: Mostrar la resta de los dos numeros")
        print("Opcion 3: Mostrar la multiplicacion de los dos numeros")
        print("Opcion 4: Salir \n")
        opc = int(input("Porfavor ingrese la opcion que desea: "))
        if opc == 1:
            numero1 = int(input("Porfavor ingrese el primer numero: "))
            numero2 = int(input("Porfavor ingrese el segundo numero: "))
            print("LA SUMA DE LOS NUMEROS ES:  ", (numero1+numero2), "\n")
        elif opc==2:
            numero1 = int(input("Porfavor ingrese el primer numero: "))
            numero2 = int(input("Porfavor ingrese el segundo numero: "))
            print("LA RESTA DE LOS NUMEROS ES: ", (numero1-numero2), "\n")
        elif opc==3:
            numero1 = int(input("Porfavor ingrese el primer numero: "))
            numero2 = int(input("Porfavor ingrese el segundo numero: "))
            print("LA MULTIPLICACION DE LOS NUMEROS ES: ", (numero1*numero2), "\n")
        elif opc == 4:
            sal = True
        else:
            print("Opcion mal ingresada")
    print("Fin")

def numImpar():
    #Actividad con bucles -- Priscila Bernal
    numero = int(input("Porfavor ingrese un numero impar: "))
    while numero % 2 == 0:  
        numero = int(input("Porfavor ingrese un numero impar: "))
    print("Gracias")

def sumarPares():
    # Ejercicio 4 -- Priscila Bernal
    print("PROGRAMA PARA SUMAR LOS 100 PRIMEROS NUMEROS PARES")
    cont = 0
    suma = 0
    while cont <= 100:
        if cont % 2 == 0:
            suma += cont
        cont += 1
    print("La suma es: ",suma)
    print("Gracias")

def calcularMedia():
    # Ejercicio 5 -- Priscila Bernal
    suma = 0
    media=0
    print("CALCULO DE LA MEDIA ARITMETICA DE VARIOS NUMEROS")
    numeros = int(input("¿Cuántos números desea ingresar: ? ") )
    for x in range(numeros):
        suma += int(input("Ingrese un número: ") )
    media=suma/numeros
    print("La media aritmética de los números ingresados es: ",media)
    print("Gracias")

def numCorrecto():
    # Ejercicio 6 --Priscila Bernal
    print("NUMERO CORRECTO")
    numeros = [1, 3, 6, 9]
    while True:
        numero = int(input("Escribe un número del 0 al 9: "))
        if numero >= 0 and numero <= 9:
            break
    if numero in numeros:
        print("El número",numero,"si se encuentra en la lista:",numeros)
    else:
        print("El número",numero,"no se encuentra en la lista:",numeros)

def imprimirListas():
    # Ejercicio 7 -- Priscila Bernal
    print("IMPRESION DE LISTAS CON RANGE")
    print("Lista 1 números del 0 al 10 : ", list(range(0, 11)))
    print("Lista 2 números del -10 al 0 : ", list(range(-10, 1)))
    print("Lista 3 números pares del 0 al 20 : ", list(range(0, 21, 2)))
    print("Lista 4 números impares entre -20 y 0 : ", list(range(-19, 0, 2)))
    print("Lista 5 números múltiples de 5 del 0 al 50 : ",list(range(0, 51, 5)))

def nuevaLista():
    # Ejercicio 8 -- Priscila Bernal
    print("GENERAR NUEVA LISTA")
    lista1 = ['h','o','l','a',' ', 'p','y','t','h','o','n']
    lista2 = ['h','o','l','a',' ', 'm','u','n','d','o']
    lista3 = []
    for letra in lista1:
        if letra in lista2 and letra not in lista3:
            lista3.append(letra)
    print("Lista 1: ", lista1)
    print("Lista 2: ", lista2)
    print("Nueva lista: ", lista3)
        
#------- Creacion del menu de opciones ----------------------
salir = False
opcion = 0
while not salir:
    print ("MENU DE OPCIONES")
    print ("1. Ejercicio 1")
    print ("2. Ejercicio 2")
    print ("3. Ejercicio 3")
    print ("4. Ejercicio 4")
    print ("5. Ejercicio 5")
    print ("6. Ejercicio 6")
    print ("7. Ejercicio 7")
    print ("8. Ejercicio 8")
    print ("9. Salir") 
    print ("Elige una opcion")
 
    opcion = pedirOpcion()
 
    if opcion == 1:
        print ("Ejercicio 1")
        diaVacaciones()
    elif opcion == 2:
        print ("Ejercicio 2")
        operacionNumeros()
    elif opcion == 3:
        print("Ejercicio 3")
        numImpar()
    elif opcion == 4:
        print ("Ejercicio 4")
        sumarPares()
    elif opcion == 5:
        print("Ejercicio 5")
        calcularMedia()
    elif opcion == 6:
        print ("Ejercicio 6")
        numCorrecto()
    elif opcion == 7:
        print("Ejercicio 7")
        imprimirListas()
    elif opcion == 8:
        print("Ejercicio 8")
        nuevaLista()
    elif opcion == 9:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 8")
print ("Gracias...")