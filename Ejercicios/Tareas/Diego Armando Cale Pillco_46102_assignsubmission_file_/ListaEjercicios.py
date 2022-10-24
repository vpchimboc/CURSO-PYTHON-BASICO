from contextlib import ExitStack


def ejercicio1():
    nombre=input("Ingrese el Nombre: ")
    clave=int(input("Ingrese la clave del Departamento:\n Clave 1\n Clave 2\n Clave 3\n >: "))
    anio=int(input("Ingrese la antiguedad en años: "))
    if clave==1:
        print("Atencion al cliente")
        if anio==1:
            print(nombre+" reciben 6 días de vacaciones")
        elif anio > 2 and anio <=6:
         print(nombre+" reciben 14 días de vacaciones") 
        elif anio >= 7: 
            print(nombre+" reciben 20 días de vacaciones")
    elif clave==2:
            print("Departamento de Logística")
   # anio=int(input("Anio de servicio: "))
            if anio==1:
                print(nombre+ " reciben 7 días de vacaciones")
            elif anio > 2 and anio <=6:
                print(nombre+" reciben 15 días de vacaciones")
            elif anio >= 7: 
                print(nombre+" reciben 30 días de vacaciones")
    elif clave==3:
            print("Gerencia ")
    #anio=int(input("Anio de servicio: "))
            if anio==1:
                print(nombre+" reciben 10 días de vacaciones")
            elif anio > 2 and anio <=6:
                print(nombre+" reciben 20 días de vacaciones")
            elif anio >= 7: 
                print(nombre+" reciben 30 días de vacaciones")

def ejercicio2():
    n1=int(input("Ingrese el número 1: "))
    n2=int(input("Ingrese el número 2: "))
    numero = int(input("Elija una opción:\nSUMA 1\nRESTA 2\nMULTIPLICACIÓN 3\n >:  "))
    if numero<=3:
        if numero==1:
            print("La SUMA es : "+str(n1+n2))
        elif numero ==2:
            print("La RESTAes : "+str(n1-n2))
        elif numero ==3:
            print("La MULTIPLICACIÓN es : "+str(n1*n2))
    else:
        print("Opcion Invalida !! ")

def ejercicio3():
    my_condition=1
    while  my_condition== 1:
        numero=int(input("Ingrese un número Impar: "))
        if numero%2!=0:
            my_condition=0
            print("El número "+str(numero)+" es Impar")

def ejercicio4():
    numero=1
    acumulador=0
    while numero <= 100:
        if numero%2==0:
            acumulador += numero  
        numero+=1  
    print("La suma de los números pasres es "+str(acumulador))

    #suma = sum(range(0,101,2))
    #print(suma)

def ejerciio5():
    print("----CALCULAR LA MEDIA-----")
    n=int(input("Cuantos numeros quiere introducir\n >: "))
    acumulador=0
    contador=1
    while contador <= n:
        x=int(input("Ingrese el numero: "))
        acumulador+=x
        contador+=1
    print("La media es "+str(acumulador/n))

def ejercicio6():
    numeros = [1, 3, 6, 9]
    my_condition=1
    bandera=True
    while bandera==True:
        numero=int(input("Ingrese un número de la Lista [1, 3, 6, 9]: "))
        if numero>=0 and numero<=9:
            bandera=False
            try:
                print("El número esta dentro de la lista en la posición "+str(numeros.index(numero)))
            except:
                print("El número NO esta dentro de la lista")

def ejercicio7():
    my_other_list=list(range(0,11))
    print("L1: ",my_other_list)
    my_other_list=list(range(-10,1))
    print("L2: ",my_other_list)
    my_other_list=list(range(0,21,2))
    print("L3: ",my_other_list)
    my_other_list=list(range(-19,-2,2))
    print("L4: ",my_other_list)
    my_other_list=list(range(0,51,5))
    print("L5: ",my_other_list)

def ejercicio8():
    lista1 = [1, 2, 3, 4, 5, 30, 17]
    lista2 = [35, 24, 62, 52, 30, 30, 17]
    my_other_list = []

    my_other_list=lista1+lista2
    my_other_list.sort()
    for elemento in lista2:
        if my_other_list.count(elemento)>1:
            my_other_list.remove(elemento)
    print("La lista Final seria :"+str(my_other_list))


def menu():
    print("---Menu de OPCIONES---")
    print("EJERCICIO > 1\nEJERCICIO > 2\nEJERCICIO > 3\nEJERCICIO > 4\nEJERCICIO > 5\nEJERCICIO > 6\nEJERCICIO > 7\nEJERCICIO > 8\nSALIR > 9 ")
    eleccion = int(input("INGRESE SU ELECCIÓN: "))
    bandera=False
    if(eleccion>=1 and eleccion<=9):
        bandera=True
    while (bandera):
        if(eleccion==1):
            ejercicio1()
            menu()
        elif eleccion==2:
            ejercicio2()
            menu()
        elif eleccion==3:
            ejercicio3()
            menu()
        elif eleccion==4:
            ejercicio4()
            menu()
        elif eleccion==5:
            ejerciio5()
            menu()
        elif eleccion==6:
            ejercicio6()
            menu()
        elif eleccion==7:
            ejercicio7()
            menu()
        elif eleccion==8:
            ejercicio8()
            menu()
        elif eleccion==9:
            break
            exit           
    else:
        print("NO estas tomando en serio el SISTEMA !!!. ")
        menu()
        exit

menu()