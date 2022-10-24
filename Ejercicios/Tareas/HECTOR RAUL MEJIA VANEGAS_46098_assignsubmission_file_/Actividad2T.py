def Calculo_Vacaciones():
    nombre=input("introducir su Nombre: ")
    departamento=int(input("ingresar la clave de su Departamento: "))
    antiguedad=int(input("ingresar su Antigüedad: "))
    if departamento==1:
        if antiguedad==1:
             print("Estimado/a",nombre,"usted tiene 6 dias de vacaciones")
        elif antiguedad>=2 and antiguedad<=6:
            print("Estimado/a",nombre,"usted tiene 14 dias de vacaciones")
        elif antiguedad>=7:
            print("Estimado/a",nombre,"usted tiene 20 dias de vacaciones")
    elif departamento==2:
        if antiguedad==1:
            print("Estimado/a",nombre,"usted tiene 7 dias de vacaciones")
        elif antiguedad>=2 and antiguedad<=6:
            print("Estimado/a",nombre,"usted tiene 15 dias de vacaciones")
        elif antiguedad>=7:
            print("Estimado/a",nombre,"usted tiene 22 dias de vacaciones")
    elif departamento==3:
        if antiguedad==1:
            print("Estimado/a",nombre,"usted tiene 10 dias de vacaciones")
        elif antiguedad>=2 and antiguedad<=6:
            print("Estimado/a",nombre,"usted tiene 20 dias de vacaciones")
        elif antiguedad>=7:
            print("Estimado/a",nombre,"usted tiene 30 dias de vacaciones")
    else:
        print("Estimado/a",nombre,"usted no pertenece a ningun departamento")
    #le damos cuerpo a nuestra funcion
 #invocamos a nuestra funcion

def Operaciones_Matematicas():
    print("OPERACIONES MATEMATICAS")
    num_1=int(input("ingresar Primer Valor: "))
    num_2=int(input("ingresar segundo Valor: "))
    print("1.SUMAR\n 2.RESTAR")
    opera=int(input("ingresar el valor de operacion a realizar: "))
    if opera==1:
        resul=num_1+num_2
        print("El resultado de la sumas es",resul)
    elif opera==2:
        resul=num_1-num_2
        print("El resultado de la resta es",resul)
    else:
        print("No a selecionado una operacion valida")

def Numeros_Impares():
    print("Numeros Impares")
    num_1=int(input("ingresar un numero Impar: "))
    resul=num_1%2
    while resul==0:
        print("El valor ingresado no es el correcto")
        num_1=int(input("ingresar nuevamente un numero Impar: "))
        resul=num_1%2
           
def Suma_Cien_Pares():
    print("SUMA DE LOS 100 NUMERO PARES")
    suma=0
    for i in range(101):
        if i%2==0:
            suma=suma+i
    print(suma)

def Media_Aritmetica():
    print("Media Aritmetica")
    num_1=int(input("ingresar un numero Numero que desea ingresar: "))
    suma=0
    valor=0
    for i in range(num_1):
        print("Ingrese el ",i+1,"valor")
        num_2=int(input("ingresar un numero Numero que desea ingresar: "))
        suma=suma+num_2
    resul=suma/num_1    
    print("La sumas es ",suma)
    print("La media Aritmentica es ",resul)

def Numero_Entero():
    print("Listas")
    num=int(input("ingresar un número entero del 0 al 9:"))
    lista=list()
    lista = [0,3,6,9]
    while num>9:
            print("El valor ingresado no es el correcto")
            num=int(input("ingresar nuevamente un número entero del 0 al 9: "))
        
    if num in lista:
        print("true")
    else:
        print("false") 

def listas():
    print("Listas")

    list1,list2,list3,list4,list5=list(),list(),list(),list(),list()

    for i in range(0,11):
     list1.append(i)

    for i in range(-10,0):
        list2.append(i)

    for i in range(0,11):
        list3.append(i*2)  

    for i in range(-20,0):
        if i%2 !=0:
            list4.append(i) 

    for i in range(0,11):
        list5.append(i*5)

    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)


while True:
     print("********************")
     print("* Menú de opciones *")
     print("********************")

     print("1.Calculo de Vacaciones")
     print("2.Operaciones(Menu)")
     print("3.Numero Impar")
     print("4.Suma enteros pares desde el 0 hasta el 100 ")
     print("5.Media Aritmetica")
     print("6.un número entero del 0 al 9")
     print("7.listas dinámicamente ")
     print("8.Lista sin repetise ningún elemento en la nueva lista ")
     val1=int(input("Introduce la opción deseada:"))
     print(val1)
     if val1==1:
        Calculo_Vacaciones()
     elif val1==2:
        Operaciones_Matematicas()
     elif val1==3:
        Numeros_Impares()
     elif val1==4:
        Suma_Cien_Pares()
     elif val1==5:
        Media_Aritmetica()
     elif val1==6:
        Numero_Entero()
     elif val1==7:
        listas()
     elif val1==8:
        print("8")
     elif val1==9:
        break
     else:
        print("Ingrese el numero correcto")
   
    