# DECLARACIÓN DE FUNCIONES

# SISTEMA PARA CALCULAR EL PROMEDIO DE UN ALUMNO
# EJERCICIO 1 

def ejercicio1():
    print("\nSISTEMA PARA CALCULAR EL PROMEDIO DE UN ALUMNO \n ")
    nombre = input("Para comenzar, Cuál es tu nombre:  \n " )
    nota_matematicas=int(input(nombre + " cuál es tu calificación en Matemáticas discretas : \n "))
    nota_introducción = float(input(nombre + " cuál es tu calificación en Introducción a desarrollo de Software : \n " ))
    nota_ingles = float(input(nombre +  " cuál es tu calificación en Inglés : \n " ))

    promedio =(nota_matematicas + nota_introducción +nota_ingles)/3

    if (promedio>=7):
        estado="Aprobaste"
        print("\nFelicitaciones ", nombre, estado , "con un promedio", promedio )
    else:
        estado="Reprobado"
        print("\nLo siento ", nombre, estado , "con un promedio", promedio )

# **********************************************************************************************************
# OPERACIONES MATEMÁTICAS
# EJERCICIO 2 

def ejercicio2():
    print("\nOperaciones Matemáticas \n")
    clave=int(1)
    while (clave!=4):
        print("\n1. Suma de dos números")
        print("2. Resta de los dos números ")
        print("3. Multiplicación de dos números")
        print("4. Salir \n")
        clave=int(input("Digite una opción: " ))
        if (clave<1 or clave>4):
            print("La opción es incorrecta, digite nuevamente")
        elif clave ==4:
            print("Gracias por usar el sistema")
        else:
            num_entero1=int(input("Ingresa el primer número: "))
            num_entero2=int(input("Ingresa el segundo número: "))
            if clave==1:
                resultado=num_entero1+num_entero2
                print("\nEl resultado de la suma es: ",resultado)
            elif clave ==2:
                resultado=num_entero1-num_entero2
                print("\nEl resultado de la resta es: ",resultado)
            else:
                resultado=num_entero1*num_entero2
                print("\nEl resultado de la multiplicación es: ",resultado)

# **********************************************************************************************************
# NÚMEROS IMPARES
# EJERCICIO 3 

def ejercicio3():
    print("\nCOMPROBACIÓN DE NÚMEROS IMPARES")
    numero=1
    while (numero>0):
        print("\nNumeros impares")
        print("Para salir digite -1")
        numero=int(input("Digite un numero impar: " ))
        if (numero%2==0):
            print("El numero es PAR, digite nuevamente")
        else:
            print("El numero es IMPAR, felicitaciones")

# **********************************************************************************************************
# SUMA DE NÚMEROS ENTEROS PARES MENORES A 100
# EJERCICIO 4

def ejercicio4():
    print("\nSUMA DE NÚMEROS ENTEROS PARES MENORES A 100\n")
    numero,suma=1,0
    while (numero<=100):
        numero=numero+1 
        if (numero%2==0):
            suma=suma+numero
    print("La suma es igual a: ",suma)


# **********************************************************************************************************
# MEDIA ARITMÉTICA
# EJERCICIO 5 

def ejercicio5():
    print("\nMEDIA ARITMÉTICA:\n")
    numero=int(input("Digite cuantos nùmeros desea ingresar: " ))
    conta, suma=0,0
    while (numero>conta):
        suma=suma+int(input("Digite un numero: " ))
        conta=conta+1
    promedio=suma/conta
    print("\nLa media aritmetica es:", promedio)


# **********************************************************************************************************
# BUSCAR NÚMERO
# EJERCICIO 6 

def ejercicio6():
    numeros = [1, 3, 6, 9]
    numero = -1
    print("\nBUSCAR NÚMERO:\n")
    while (numero<0 or numero>9):
        numero=int(input("Digite un numero entero de 0 a 9: " ))
    
    if numero in numeros:
        print("El numero: ", numero,  " se encuentra en la lista" , numeros)
    else:
        print("El numero: ", numero,  " no se encuentra en la lista adios" , numeros)

# **********************************************************************************************************
# OPERACIONES MATEMÁTICAS
# EJERCICIO 7

def ejercicio7():
    print("\nEJEMPLOS DE RANGE\n")
    print("Todos los números del 0 al 10 [0, 1, 2, ..., 10]\n")
    x=range(11)
    print(list(x))

    print("\nTodos los números del -10 al 0 [-10, -9, -8, ..., 0]\n")
    x=range(-10,1)
    print(list(x))

    print("\nTodos los números pares del 0 al 20 [0, 2, 4, ..., 20]\n")
    x=range(0,22,2)
    print(list(x))

    print("\nTodos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]\n")

    x=range(-19,0,2)
    print(list(x))

    print("\nTodos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]\n")
    x=range(0,55,5)
    print(list(x))

# **********************************************************************************************************
# LISTAS
# EJERCICIO 8

def ejercicio8():

    l1 = [1,5,7,11]
    l2 = [0,2,2,4,6,8,9,11,15,19,23,1]
    l3 = []
    print("\nNÚMEROS QUE SE REPITEN EN LISTAS")
    for num in l1:
        if ((num in l2) and (num not in l3)):
            l3.append(num)

    print("\nLos números que se repiten en la lista l1:  ",l1, " y la lista l2: ",l2, " son: ", l3)



# **********************************************************************************************************
# ACTIVIDAD NÚMERO 2
clave=1
while (clave!=9):
    print("\n1. ACTIVIDAD 2")
    print("\n1. Ejercicio 1")
    print("2. Ejercicio 2 ")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Ejercicio 8")
    print("9. Salir \n")
    clave=int(input("Digite una opción: " ))
    if (clave<1 or clave>9):
        print("La opción es incorrecta, digite nuevamente")
    elif clave ==9:
        print("Gracias por usar el sistema")
    else:
        if clave==1:
            ejercicio1()
        if clave==2:
            ejercicio2()
        if clave==3:
            ejercicio3()
        if clave==4:
            ejercicio4()
        if clave==5:
            ejercicio5()
        if clave==6:
            ejercicio6()
        if clave==7:
            ejercicio7()
        if clave==8:
            ejercicio8()



   
       

