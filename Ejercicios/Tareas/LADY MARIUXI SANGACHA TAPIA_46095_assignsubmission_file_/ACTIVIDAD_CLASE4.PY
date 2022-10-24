
#@CREADO Y MODIFICADO POR LADY SANGACHA  
########CREAR UN MENU CON TODOS LOS EJERCICIOS DE LA ACTIVIDAD 
########APLICANDO FUNCIONES


def mostrar_menu(opciones):
    print("\n############# MENU DE OPCIONES LEYDYCA #########")
    print("Seleccione una opción:")
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Opción 1: ACTIVIDAD 1', accion1),
        '2': ('Opción 2: ACTIVIDAD 2', accion2),
        '3': ('Opción 3: ACTIVIDAD 3', accion3),
        '4': ('Opción 4: ACTIVIDAD 4', accion4),
        '5': ('Opción 5: ACTIVIDAD 5', accion5),
        '6': ('Opción 6: ACTIVIDAD 6', accion6),
        '7': ('Opción 7: ACTIVIDAD 7', accion7),
        '8': ('Opción 8: ACTIVIDAD 8', accion8),
        '9': ('Salir', salir)
    }

    generar_menu(opciones, '9')

######## ACTIVIDAD 1 ########################
def accion1():
    print("USTED SELECCIONO EL EJERCICIO 1")
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

######## ACTIVIDAD 2 ########################
def accion2():
     print("USTED SELECCIONO EL EJERCICIO 2")
     n1=int(input("Ingrese el número 1: "))
     n2=int(input("Ingrese el número 2: "))
     numero = int(input("AHORA Elija una opción:\nSUMA 1\nRESTA 2\nMULTIPLICACIÓN 3\n >:  "))
     if numero<=3:
        if numero==1:
            print("La SUMA es : "+str(n1+n2))
        elif numero ==2:
            print("La RESTAes : "+str(n1-n2))
        elif numero ==3:
            print("La MULTIPLICACIÓN es : "+str(n1*n2))
     else:
         print("Opcion Invalida !! ")

 ######## ACTIVIDAD 3 ########################    
def accion3():
     print("USTED SELECCIONO EL EJERCICIO 3")
     my_condition=1
     while  my_condition== 1:
         numero=int(input("Ingrese un número Impar: "))
         if numero%2!=0:
             my_condition=0
             print("El número "+str(numero)+" es Impar")

######## ACTIVIDAD 4 ########################

def accion4():
        print("USTED SELECCIONO EL EJERCICIO 4")
        numero=1
        acumulador=0
        while numero <= 100:
         if numero%2==0:
            acumulador += numero  
            numero+=1  
            print("La suma de los números pasres es "+str(acumulador))
######## ACTIVIDAD 5 ########################
def accion5():
     print("USTED SELECCIONO EL EJERCICIO 5")
     numero=int(input("Ingrese la cantidad de números que desea ingresar : "))
     total=0
     for i in range(0,numero):
        num=int(input("Ingrese el número "+str(i)+" :"))
        total=total+num
        media=total/numero
        print("La media de los números ingresados es : ",media)

######## ACTIVIDAD 6 ########################     
def accion6():
     print("USTED SELECCIONO EL EJERCICIO 6")
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



######## ACTIVIDAD 7 ########################
def accion7():
     print("USTED SELECCIONO EL EJERCICIO 7")
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

######## ACTIVIDAD 8 ########################     
def accion8():
     print("USTED SELECCIONO EL EJERCICIO 8") 
     lista_1 = [0, 2, 3, 4, 5, 10, 27]
     lista_2 = [50, 24, 72, 52, 30, 10, 27]
     my_other_list = [] #Funcion de la lista
     my_other_list=lista_1+lista_2
     my_other_list.sort()
     for rango in lista_2:
        if my_other_list.count(rango)>1:
            my_other_list.remove(rango)
     print("\nMI TERCERA LISTA FINAL ES :"+str(my_other_list))

######## SALIDA DEL SISTEM ########################
def salir():
    print('SALIENDO DEL SISTEMA........')



if __name__ == '__main__':
 menu_principal()