def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for i in sorted(opciones):
        print(f' {i}) {opciones[i][0]}')


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


def menu():
    opciones = {
        '1': ('Ejercicio 1', ejercicio1),
        '2': ('Ejercicio 2', ejercicio2),
        '3': ('Ejercicio 3', ejercicio3),
        '5': ('Ejercicio 5', ejercicio5),
        '6': ('Ejercicio 6', ejercicio6),
        '4': ('Ejercicio 4', ejercicio4),
        '7': ('Ejercicio 7', ejercicio7),
        '8': ('Ejercicio 8', ejercicio8),
        '9': ('Salir', salir)
    }
    generar_menu(opciones, '9')


def ejercicio1():
    print('Has elegido la opción 1')
    nombre = input("Por favor ingrese su nombre: ")
    print("Lista de Departamentos:\n \t 1. Departamento de Atención al Cliente \n \t 2. Departamento de Logística \n \t 3. Gerencia  ")
    dep = int(input("Por favor " +nombre+ " Ingrese el Numero de Departamento al que pertenece: "))
    aser=int(input("Ingrese los años de servicio en el departamento:"))
    if(dep==1 and aser==1):
        mensaje=nombre  + " :Tienes 6 dias de vacaciones"
    elif (dep==1 and aser>=2 and aser<=6):
        mensaje=nombre+ " :Tienes 14 dias de vacaciones"
    elif (dep==2 and aser==1 ):
        mensaje=nombre+ " :Tienes 7 dias de vacaciones"
    elif (dep==2 and aser>=2 and aser<=6):
        mensaje=nombre+ " :Tienes 15 dias de vacaciones"
    elif (dep==2 and aser>=7):
        mensaje=nombre+ " :Tienes 22 dias de vacaciones"
    elif (dep==3 and aser==1 ):
        mensaje=nombre+ " :Tienes 10 dias de vacaciones"
    elif (dep==3 and aser>=2 and aser<=6):
        mensaje=nombre+ " :Tienes 20 dias de vacaciones"
    elif (dep==3 and aser>=7):
        mensaje=nombre+ " :Tienes 30 dias de vacaciones"
    elif(dep!=1 or dep!=2 or dep!=3 ):
        mensaje="Error de departamento"
    print(mensaje)


def ejercicio2():
    print("Seleccione la operacion>\n \t 1. SUMA \n \t 2. RESTS \n \t 3. MULTIPLICACION  ")
    opt = int(input("Ingrese la operacion"))
    n1 = int(input("Por favor, ingrese un numero"))
    n2 = int(input("Por favor, ingrese otro numero"))
    if(opt==1):
        print(n1+n2)
    elif(opt==2):
        print(n1-n2)
    elif(opt==3):
        print(n1*n2)
    else:
        print("Opcion no valida")

def ejercicio3():
    print("INGRESA UN NUMERO")
    numero = 0
    while numero % 2 == 0: 
        numero = int(input("ERROR, Ingresa  un número IMPAR: ") )
    print("CORRECTO EL NUMERO  ES  PAR")

def ejercicio4():
    print("EJERCICIO 4") 
    suma=0;
    for i in range(0,101,2):
        suma=suma+i
    print(suma)


def ejercicio5():
    print(":::::::::::::::::::::::::::::::::::")
    print("Ejericio 5")
    n1 = int(input("Por favor, cuantos numero desea sumar"))
    c=0
    ma=0
    while n1!=c:
        n2 = int(input("Por favor, ingrese un numero: "))
        c=c+1
        ma=ma+n2
    print("La Media es:  " + str(ma/n1))

def ejercicio6():
    print("EJERCICIO 6")
    
    n = int(input("Por favor, ingrese un numero:"))
    c=4
    lista = list()
    while n!=c:
        
        lista.append(n)
        n = int(input("Por favor, ingrese un numero"))
        if n in lista:
            print("El numero ya existe")
        
    print("Ha terminado el numero era: "+str(c))
    print("Los numeros ingresados son:"+ str(lista))

def ejercicio7():
    print("EJERCICIO 6")
    lista = list()
    lista2 = list()
    lista3=list()
    lista4=list()
    lista5=list()
    for i in range(0,11):
        lista.append(i)
    print("Lista de numeros de 0 al 10"+str(lista))
    for i in range(-10,1):
        lista2.append(i)
    print("Lista de numeros de -10 al 0: "+str(lista2))
    for i in range(0,21,2):
        lista3.append(i)
    print("Todos los números pares del 0 al 20:"+str(lista3))
    for i in range(-19,0,2):
        lista4.append(i)
    print("	Todos los números impares entre -20 y 0:"+str(lista4))
    for i in range(0,50,5):
        lista5.append(i)
    print("	•	Todos los números múltiples de 5 del 0 al 50: "+str(lista5))

def ejercicio8():
    print("EJERCICIO 8")
    a = [1,2,3,4,5,6,7]
    b = [9,8,7,3,3,6,5,4]
    resultado = list()

    
    resultado=[]
    for i in a:
            for j in b:
                if i==j:
                    if i not in resultado: # verificamos que no se encuentre en la lista
                        resultado.append(i)
    print("La lista a es:  " +str(a) )
    print("La lista b es:  "+ str(b))
    print("La lista resultante es :  "+ str(resultado))

def salir():
    print('Saliendo')
    


if __name__ == '__main__':
    menu()