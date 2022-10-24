from tkinter import Variable


condicion = 0
while condicion == 0: 
    print("EJERCICIOS DE LA ACTIVIDAD 2")
    print("++++++++++++++++++++++++++++++++")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Ejercicio 8")
    print("9. SALIR")
    numero = int(input("Introduce la opcion deseada: "))
    def ej1():
        print("SISTEMA WT: EMPLEADOS POR CLAVE Y ANTIGUEDAD")
        NOMBRE=input("Cual es su Nombres y Apellidos: ")
        CLAVE=int(input("Cual es su CLAVE: "))
        ANTIGUEDAD=int(input("Cual es su antiguedad "))
        if CLAVE == 1:
            print("ATENCION")
            if ANTIGUEDAD == 1:
                print("6 dias de VACACIONES")
            elif ANTIGUEDAD > 1 and ANTIGUEDAD <= 6:
                print("15 dias de VACACIONES")
            else:
                print("22 dias de VACACIONES")

        elif CLAVE == 2:
            print("LOGISTICA")
            if ANTIGUEDAD == 1:
                print("7 dias de VACACIONES")
            elif ANTIGUEDAD > 2 and ANTIGUEDAD <= 6:
                print("15 dias de VACACIONES")
            else: 
                print("22 dias de VACACIONES")

        elif CLAVE == 3:
            print("GERENCIA")
            if ANTIGUEDAD == 1:
                print("10 dias de VACACIONES")
            elif ANTIGUEDAD > 2 and ANTIGUEDAD <= 6:
                print("20 dias de VACACIONES")
            else:
                print("30 dias de VACACIONES")
    def ej2():
        condicion = 0
        while condicion == 0: 
            print("SISTEMA WT: RESTA Y MULTIPLICACION")
            print("Para poder realizar este sistema ingrese los siguientes numeros")
            n1 = input("Ingrese el primer numero ")
            n2 = input("Ingrese el segundo numero ")
            opcion = int(input("1: Mostrar una resta de los dos números (el primero menos el segundo)\n2: Mostrar una multiplicación de los dos \n3: SALIR \nEscoja una opcion "))

            if opcion == 1:
                print("RESTA DE LOS DOS NUMEROS")
                print("El resultado es "+ str(int(n1)-int(n2)))
            elif opcion == 2:
                print("LA MULTIPLICACION DE LOS DOS NUMEROS")
                print("El resultado es "+ str(int(n1)*int(n2)))
            elif opcion == 3:
                print("SALIR")
                break
    def ej3():
        va = 0
        while va == 0: 
            print("SISTEMA WT: NUMEROS IMPARES")
            valor =int(input("Ingrese un numero Impar: "))
            if valor% 2 > 0:
                print("Ingresado Correctamente")
                break
            else:
                print("Incorrecto: Ingrese un numero impar")    
    def ej4():
        print("SISTEMA WT: SUMA DE TODOS LOS NUMEROS PARES DEL 0 HASTA EL 100")
        total = 0
        for i in range(0,102,2):
            total = total +i
            print(str(i)+"==="+str(total))
        print("TOTAL DE PARES ES: "+str(int(total)))
    def ej5():
        print("SISTEMA WT: LA MEDIA ARITMETICA")
        numero = int(input("Cuantos numeros desea ingresar: "))
        total = 0
        for i in range(numero):
            var= i+1
            dato = int(input("Ingrese el valor "+ str(var)+ ": "))
            total+=dato
        print("La media aritmetica es: "+ str(total/numero))
    def ej6():
        cont = 0
        while(cont == 0):
            print("SISTEMA WT")
            valor = int(input("Ingresar un numero entero entre el 0 al 9: "))
            NUMEROS = [0,1,2,3,4,5,6,7,8,9]
            for num in NUMEROS:
                if (valor == num):
                    indice = NUMEROS.index(valor)
                    cambiar = int(input("Ingresar el numero a cambiar: "))
                    NUMEROS[indice]= cambiar
                    print(NUMEROS)
            sal = int(input("Desea Salir digite el numero 59:, sino presione otro numero:  "))
            if(sal==59):
                cont=1
    def ej7():
            print("TODOS LOS NUMEROS DEL 0 AL 10")
            print(list(range(0,11)))
            print("TODOS LOS NUMEROS DEL -10 A 1")
            print(list(range(-10,0)))
            print("TODOS LOS NUMEROS PARES DEL 0 A 20")
            print(list(range(0,20,2)))
            print("TODOS LOS NUMEROS IMPARES DEL -20 A 0")
            print(list(range(-19,0,2)))
            print("TODOS LOS MULTIPLOS DEL 5 DESDE EL 0 AL 50")
            print(list(range(0,51,5)))
    def ej8():
        lis1=[]
        lis2=[]
        lis3=[]
        vare=0
        numero = int(input("Cuantos datos desea ingresar en las listas: "))
        total = 0
        for i in range(numero):
            vare= i+1
            con1=0
            while con1==0:
                dato = int(input("Ingrese el valor "+ str(vare)+ " de la lista 1: ")) 
                if dato in lis1:
                    print("Numero ya ingresado")
                else:
                    lis1.append(dato)
                    con1=1
        for i in range(numero):
            vare= i+1
            con2=0
            while con2==0:
                dato = int(input("Ingrese el valor "+ str(vare)+ " de la lista 2: ")) 
                if dato in lis2:
                    print("Numero ya ingresado")
                else:
                    lis2.append(dato)
                    con2=1
        for lista in lis1:
            if lista in lis2:
                lis3.append(lista)
        print("LISTA 3 DE LOS REPETIDOS: ",lis3)
    if numero== 1:
        ej1()
    elif numero == 2:
        ej2()
    elif numero == 3:
        ej3()
    elif numero == 4:
        ej4()
    elif numero == 5:
        ej5()
    elif numero == 6:
        ej6()
    elif numero == 7:
        ej7()
    elif numero == 8:
        ej8()
    elif numero == 9:
        condicion =1
        break
    else:
        print("INGRESE UN NUMERO QUE ESTE DENTRO DEL RAGO 1 AL 8")