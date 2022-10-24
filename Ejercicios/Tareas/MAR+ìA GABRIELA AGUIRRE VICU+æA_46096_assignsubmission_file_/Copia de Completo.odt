#TAREA 2 COMPLETO
#GABRIELA AGUIRRE

# EJERCICIO 1
def ejercicio1():
    nombre=input("Cual es tu nombre : ")
    clave=int(input("Ingrese la clave : "))
    antiguedad=int(input("Ingrese la antiguedad en años : "))
    print(nombre,clave,antiguedad)
    if clave==1:
            if antiguedad==1:
                print(nombre+" te corresponde 6 días de vacaciones")
            elif antiguedad<=14:
                print(nombre+" te corresponde 14 días de vacaciones")
            else:
                print(nombre+" te corresponde 20 días de vacaciones")
    elif clave==2:
            if antiguedad==1:
                print(nombre+" te corresponde 7 días de vacaciones")
            elif antiguedad<=6:
                print(nombre+" te corresponde 15 días de vacaciones")
            else:
                print(nombre+" te corresponde 22 días de vacaciones")
    elif clave==3:
            if antiguedad==1:
                print(nombre+" te corresponde 10 días de vacaciones")
            elif antiguedad<=6:
                print(nombre+" te corresponde 20 días de vacaciones")
            else:
                print(nombre+" te corresponde 30 días de vacaciones")
    else:
        print("fin")

# EJERCICIO 2
def ejercicio2():
    numero1=int(input("Ingrese el número 1 : "))
    numero2=int(input("Ingrese el número 2 : "))
    print("OPERACIONES")
    print("1- Resta")
    print("2- Multiplicación")
    print("3- Salir")
    opcion=int(input("Seleccione una opción : "))
    if opcion==1:
            resultado=numero1-numero2
            print("El resultado de la resta es :"+str(resultado))
    elif opcion==2:
            resultado=numero1*numero2
            print("El resultado de la multiplicación es :",resultado)

    else:
        print("Gracias")

# EJERCICIO 3
def ejercicio3():
    band=1
    while band==1:
        numero=int(input("Ingrese un número impar : "))
        par=numero%2
        print(par)
        if par==0:
            print("El numero ingresado es incorrecto :"+str(numero))
        else:
            print("El numero ingresado es correcto :"+str(numero))
            band=0
    else:
        print("Fin")

# EJERCICIO 4
def ejercicio4():
    suma=0
    for i in range(0,100,2):#inicia en 0, hasta 100 incremento de 2
        suma+=i
        print(i)
    print("El resultado de la suma es : ",suma)

# EJERCICIO 5
def ejercicio5():
    numero=int(input("Ingrese la cantidad de números que desea ingresar : "))
    total=0
    for i in range(0,numero):
        num=int(input("Ingrese el número "+str(i)+" :"))
        total=total+num
    media=total/numero
    print("La media de los números ingresados es : ",media)

# EJERCICIO 6
def ejercicio6():
    numeros= [1, 3, 6, 9]
    band=0
    while band==0:
        num=int(input("Ingrese un numero entero entre 0 y 9 : "))
        #print(num)
        if num>=0 and num<=9:
            band=1
            if num in numeros:
                print("Se encuentra dentro de la lista")
            else:
                print("No se encuentra dentro de la lista")  
        else:
            print("numero incorrecto")

# EJERCICIO 7
def ejercicio7():
    print("Lista 1\n")
    for a in range(0,11,1):
        print(a,end=" ")
    print("\n\nLista 2\n")
    for b in range(-10,0,1):
        print(b,end=" ")
    print("\n\nLista 3\n")
    for c in range(0,22,2):
        print(c,end=" ")
    print("\n\nLista 4\n")
    for d in range(-19,0,1):
        print(d,end=" ")
    print("\n\nLista 5\n")
    for e in range(0,55,5):
        print(e,end=" ")
    print("\n\nFIN")

# EJERCICIO 8
def ejercicio7():
    lista1=["paco","pepe","luis","diego"]
    lista2=["diego","mari","luis","gaby"]
    comparacion = []
    
    for i in lista1:
        if i in lista2:
            comparacion.append(i)
    
    if len(comparacion) > 0:
        print ("Ambas listas contienen estos elementos")
    for j in comparacion: print ("%s" % j)
    else:
        print ("No existe ningun elemento igual en las listas")

# MAIN
opc=0
while opc!=9:
    print("*****************")
    print("***    MENU   ***")
    print("*****************")
    print("1.- VACACIONES")
    print("2.- SUMA")
    print("3.- NUMERO IMPAR")
    print("4.- SUMA NUMEROS ENTEROS")
    print("5.- PROMEDIO")
    print("6.- LISTA NUMEROS")
    print("7.- LISTA RANGE")
    print("9.- FIN")
    opc=int(input("Ingrese la opcion :"))
    if opc==1:
        ejercicio1()
    if opc==2:
        ejercicio2()
    if opc==3:
        ejercicio3()
    if opc==4:
        ejercicio4()
    if opc==5:
        ejercicio5()
    if opc==6:
        ejercicio6()
    if opc==7:
        ejercicio7()
    if opc==9:
        print("***FIN***")
        opc=9
