# FUNCIONES
# EJERCICIO 1
def ejercicio1():

    # Ingreso de datos
    # Variables
    dep1 = "Atencion al Cliente"
    dep2 = "Logistica"
    dep3 = "Gerencia"

    # Ingreso de datos
    clave = int(input("Ingrese la clave del departamento:"))


    if clave == 1:
        print(dep1)
        tiempo = int(input("Ingrese los años de trabajo: "))
        if tiempo >= 1 and tiempo < 2:
            print("Tiene vacaciones de 6 días ")
        elif tiempo >= 2 and tiempo <= 6:
            print("Tiene vacaciones de 14 días ")
        elif tiempo >= 7:
            print("Tiene vacaciones de 20 días ")
        else:
            print("No hay vacaciones")

    elif clave == 2:
        print(dep2)
        tiempo = int(input("Ingrese los años de trabajo: "))
        if tiempo >= 1 and tiempo < 2:
            print("Tiene vacaciones de 7 días ")
        elif tiempo >= 2 and tiempo <= 6:
            print("Tiene vacaciones de 15 días ")
        elif tiempo >= 7:
            print("Tiene vacaciones de 22 días ")
        else:
            print("No hay vacaciones")

    elif clave == 3:
        print(dep3)
        tiempo = int(input("Ingrese los años de trabajo: "))
        if tiempo >= 1 and tiempo < 2:
            print("Tiene vacaciones de 10 días ")
        elif tiempo >= 2 and tiempo <= 6:
            print("Tiene vacaciones de 20 días ")
        elif tiempo >= 7:
            print("Tiene vacaciones de 30 días ")
        else:
            print("No hay vacaciones")
    else:
        print("No existe, clave incorrecta")

#EJERCICIO 2
def ejercicio2():
    print("Opreación con dos números: ")
    num1=int(input("Ingrese el primer número: "))
    num2=int(input("Ingrese el segundo número: "))
    print("Seleccione la operación que desee hacer:")
    print("1. Suma")
    print("2. Resta")
    print("3.Multiplicación")

    operacion=int(input("Digite la operación deseada: "))

    if operacion==1:
        print("La suma es: ",num1+num2 )
    elif operacion ==2:
        print("La resta es: ",num1-num2)
    elif operacion ==3:
        print("La multiplicacipon es: ", num1*num2)
    else:
        print("La opción ingresada no existe!! "+"; numero ingresado:", operacion)

#EJERCICIO 3
def ejercicio3():
    num1=int(input("Ingrese el numero: "))
    while num1%2 ==0:
        num1=int(input("Ingrese un numero impar: "))
    print("Felicidadeds!! Usted salió del bucle")

#EJERCICIO 4
def ejercicio4():
    num=0
    suma=0
    cont=100
    print(num) 
    while num <cont:
        num+=1
        print(num)    
        suma+=num
    print("Suma de 100 numeros: ", suma)

#EJERCICIO 5
def ejercicio5():
    cont=int(input("Digite el numero de datos que desea ingresar: "))
    num=0
    suma=0
    while num!=cont:
        dato=int(input("Ingrese el numero: "))
        suma+=dato
        num+=1
        media=suma/cont
    print("La media aritmética es: ",media)
#EJERCICIO 6
def ejercicio6():
    num=int(input("Ingrese un numero en el rango de 0-9:"))
    cont=0
    condicion=True
    while condicion:
        if  num in range(0,10):
            print("El ",num, " se encuentra en el rango establecido.")
            condicion=False
        elif  num >=10 or num<0:
        
            print("No en rango")
            num=int(input("Ingrese un numero en el rango de 0-9:"))
#EJERCICIO 7
def ejercicio7():
    print("Naturales: ",list(range(0,10)))
    print("Negativos: ",list(range(-10,0)))
    print("Pares: ",list(range(0,20,2)))
    print("Impares: ",list(range(-19,0,2)))
    print("Multiplos: ",list(range(0,51,5)))
#EJERCICIO 8
def ejercicio8():
    lista1=[]
    lista2=[]
    lista3=[]

    cont=0
    cont2=0
    num=int(input("Ingrese la cantidad de datos de primera lista: "))
    elemento=" "
    for listado in range(num):
        elemento=input("Ingrese el elemento "+str(listado)+":")
        lista1.append(elemento)
        cont+=1
        if cont==num:
            num2=int(input("Ingrese la cantidad de datos de la segunda lista: "))
            for listado in range(num2):
                elemento=input("Ingrese el elemento "+str(listado)+":")
                lista2.append(elemento)
                cont2+=1
                if cont2==num2:
                    print("Lista 1: ",lista1)
                    print("Lista 2: ",lista2)
                    for listado in lista1:
                        if listado in lista2:
                            lista3.append(listado)
                    print("Lista 3: ",lista3)
# Cada ejercicio es un método
def menu():
    print("BIENVENIDO A TAREA 2!!")
    print("Le presentamos el menu de actividades:")
    print("*****************************************************************")
    print("1.-Los días de vacaciones a los que tiene derecho un trabajador")
    print("2.-Programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú")
    print("3.-Programa que lea un número impar por teclado.")
    print("4.-Programa que sume todos los números enteros pares desde el 0 hasta el 100")
    print("5.-Programa que lee todos los números ingresados y realizar una media aritmética:")
    print("6.-Programa que pida al usuario un número entero del 0 al 9.")
    print("7.-Conversión a listas")
    print("8.-Generar nueva lista")
    print("Nota: Para finalizar el programa presione '0'")
    print("*****************************************************************")

#EJECUCIÓN DE MÉTODOS
menu()
opcion = int(input("Digite la opción: "))

while opcion<0 or opcion>8:
    if opcion==0:
        print("Fin del programa!!")
        break
    else: opcion=int(input("Opción no permitida, ingrese un numero del 1 al 8, o presione 0 para terminar el programa: "))
else:
    while opcion!=0:
        if opcion == 1:
            print("*** Ejercicio 1 *** ")
            ejercicio1()

        elif opcion == 2:
            print("*** Ejercicio 2 ***")
            ejercicio2()
        elif opcion == 3:
            print("**** Ejercicio 3 **** ")
            ejercicio3()
        elif opcion == 4:
            print("*** Ejercicio 4 ***")
            ejercicio4()
        elif opcion == 5:
            print("*** Ejercicio 5 ***")
        elif opcion == 6:
            print("*** Ejercicio 6 ***")
            ejercicio6()
        elif opcion == 7:
            print("Ejercicio 7")
            ejercicio7()
        elif opcion == 8:
            print("*** Ejercicio 8 ***")
            ejercicio8()
        elif opcion<0 or opcion>8:
            opcion =int(input("Opción incorrecta, ingrese un numero entre 1-8, o presione 0 para terminar el programa: "))
            if opcion==0:
                print("Fin de programa!")
                break
        opcion = int(input("Ingrese una nueva opción, o presione '0' para finalizar el programa: "))
    else :
         print("Fin de programa!")
            
        
   
