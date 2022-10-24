###  Resolución de la actividad 2 ###
   ### Desarrollado por Carmen Tacuri

###FUNCIONES###

#--------------------------------------------------------------------------------   
#Dias de vacaciones de la compañía multinacional Rap
def ejercicio1():
   ###  Sistema de calculo de vacaciones de la empresa MULTINACIONAL RAP ###
     
   # Entrada de datos
   print('----------------------------------')
   print("Bienvenido al ejercicio 1 ''Sistema Multinacional Rap''")
   print('----------------------------------')
   print('\n')
   name = input('¿Cuál es el nombre del empleado? ')
   
   condicion =True
   while (condicion ==True):
      try:      
         print('')
         print('\n')
         age = int(input('¿Cuántos años de servicio tiene el empleado '+ name + ' en la empresa? \n Ingrese un dato numérico ==>>'))
         
         if (age<1 or age >70):
            print('Debe ingresar un número entre 1 y 70 años')
                   
            condicion =True
         else:
            condicion =False
          
      except ValueError:
         condicion =True
   
   
   condicion1 =True
   
   while (condicion1 ==True):
      try:      
         print('\n')
         departamento = int(input ('¿A qué departamento pertence el empleado '+ name + '? \n \t 1. Departamento de Atención al Cliente. \n \t 2. Departamento de Logística  \n \t 3. Gerencia . \n Escoja 1 o 2 o 3: ==>> '))
         
         if (departamento == 1):
            clave =1
            condicion1 = False
         elif (departamento == 2):
            clave = 2
            condicion1 = False
         elif (departamento ==3): 
            clave = 3      
            condicion1 = False
            
         else:
            condicion1 =True
          
      except ValueError:
         condicion1 =True
        
   print('\n')
   if (clave ==1):
      if (age==1):
         print(name + ',  tiene 6 dia de vacaciones')
      elif (age >=2 and age<=6):
         print(name + ',  tiene 14 dias de vacaciones')
      elif (age >7):
         print(name + ',  tien 20 dias de vacaciones')
   elif (clave ==2):
      if (age==1):
               print(name + ',  tiene 7 dia de vacaciones')
      elif (age >=2 and age<=6 ):
         print(name + ',  tiene 15 dias de vacaciones')
      else:
         print('no es ha establecido vacaciones para este caso')    
   elif (clave == 3):
      if (age==1):
         print(name + ',  tiene 10 dia de vacaciones')
      elif (age >=2 and age<=6 ):
         print(name + ',  tiene 20 dias de vacaciones')
      elif (age >=7):
         print(name + ',  tien 30 dias de vacaciones') 
   print('FIN, muchas gracias')     
#--------------------------------------------------------------------------------   
#Calculadora
def ejercicio2():
   print('----------------------------------')
   print ('2) Programa que lee dos números por teclado y permite elegir entre 3 opciones en un menú:')
   print('----------------------------------')
   print('\n')

        
   condicion =True
   while (condicion ==True):
      try:      
         print('\n')
         numero_uno = int(input('Ingrese su primer número:  ==>> '))
         
         condicion =False
          
      except ValueError:
         condicion =True
   
   condicion =True
   while (condicion ==True):
      try:      
         print('\n')
         numero_dos = int(input('Ingrese su segundo número: ==>> '))
         
         condicion =False
          
      except ValueError:
         condicion =True
   
   condicion =True
   while (condicion ==True):
      try:      
         print('\n')
         opcion = int(input (' Escoja una opción para la operación a realizar \n \t 1. Sumar los dos numeros ingresados \n \t 2. Restar los dos numeros ingresados \n \t 3. Multiplicar los dos numeros ingresados \n Escoja 1 o 2 o 3:  ==>>  '))
         if (opcion <1 or opcion >3):
            condicion =True       
         else: condicion =False
          
      except ValueError:
         condicion =True
         
   if (opcion ==1):
          print("La suma de " + str(numero_uno) + " + " + str(numero_dos) +" es: "+ str(numero_uno + numero_dos))
   elif (opcion ==2):
      print("La resta de " + str(numero_uno) + " - " + str(numero_dos) +" es: "+ str(numero_uno - numero_dos))
   elif (opcion ==3):
      print("La multiplicacion de " + str(numero_uno) + " * " + str(numero_dos) +" es: "+ str(numero_uno * numero_dos))
   else: print("La opción seleccionada no es válida!")
   
   
   print('FIN, muchas gracias')  
      
#Ingreso de numero impar
def ejercicio3():
   print('----------------------------------')
   print ('3) Programa que lee un número impar por teclado. Si el usuario no introduce un número impar, se repete el proceso hasta que introduzca correctamente.')

   print('----------------------------------')
   print('\n')

   my_condition =True

   while (my_condition ==True):
      
      numero_impar = int(input('Ingrese un numero impar: '))
      
      if (numero_impar % 2 ==0):
         my_condition =True
         print("Debe ingresar un número impar!")
      else:
         print("Lo logró!!")
         print('FIN, muchas gracias')   
         my_condition =False

    
#Sume de todos los números enteros pares desde el 0 hasta el 100
def ejercicio4():
   print('----------------------------------')
   print ('4) Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:')

   print('----------------------------------')
   print('\n')

   numero = 0
   suma = 0
   while (numero <=100):
      
      residuo =  numero % 2
         
      if (residuo == 0):
         suma =suma + numero
               
      numero += 1
   print("La suma total de todos los numero enteros pares desde el 0 hasta el 100 es :" + str(suma)) 
   print('FIN, muchas gracias')   
    
#Media Aritmetica
def ejercicio5():
   print('----------------------------------')
   print ('5) Solicita al usuario una cantidad de numeros y devuelve la media aritmetica de ellos. ')
   print('----------------------------------')
   print('\n')
   
   condicion =True
   while (condicion ==True):
      try:      
        
         cantidad = int(input('Ingrese la cantidad de numeros a sacar la media aritmetica: (Debe ser un numero entero positivo mayor a cero) ==>> '))
         if (cantidad <=0):
                condicion =True
         else:
            condicion =False
                        
            
      except ValueError:
         condicion =True
   
   
   condicion =True
   my_other_list = []
   
   cont =0
   while (condicion ==True):
      try:      
         numero = int(input('Ingrese el numero ==>> '))
         my_other_list.insert(cont, numero)          
         cont= cont+1  
         if (cont <= cantidad -1):                
               condicion =True   
         else: condicion =False 
         
      except ValueError:
         condicion =True    
   
   print('Los numeros ingresados son: ' + str( my_other_list))
   condicion =True 
   cont =-1
   suma =0
   while (condicion ==True):
      cont = cont +1
      suma = suma + my_other_list[cont]
      if (cont == cantidad-1):
         condicion =False 
      else: condicion =True 
   
   print ('La media aritmética de los numeros ingresados es: ==>>' + str(suma/cantidad))
   print('FIN, muchas gracias')  
   
#Realiza un programa que pida al usuario un número entero del 0 al 9, 
# y que mientras el número no sea correcto se repita el proceso. 
# #Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
def ejercicio6():
   print('----------------------------------')
   print ('6) Solicita un numero entre 0 y 9, e indica si se encuentra en la lista   [1, 3, 6, 9] ')
   print('----------------------------------')
   print('\n')
   numeros=[1, 3, 6, 9]
   
   condicion=True
   while (condicion ==True):
      try:      
         numero = int(input('Ingrese un numero entero entre 0 y 9 para comprobar si esta en la lista  [1, 3, 6, 9]  ==>> '))           
         
         if (numero <0 or numero >9):                
               condicion =True   
         else: condicion =False 
         
      except ValueError:
         condicion =True
   
   encontro = numero in numeros
   if encontro==True:
         print ('El numero ' + str(numero) + ' se encuentra en la lista.')
   else: 
      print ('El numero ' + str(numero) + ' no se encuentra en la lista.')
      print('FIN, muchas gracias')  
    
#) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
#)	Todos los números del 0 al 10 [0, 1, 2, ..., 10]
#)	Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
#)	Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
#)	Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
#)	Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

def ejercicio7():
   print('----------------------------------')
   print ('7) Generación de listas')
   print('----------------------------------')
   print('\n')
   
   print('Todos los números del 0 al 10 [0, 1, 2, ..., 10]')
   numeros = list( range(0,11))
   print (numeros)
   print('\n')
   
   print('Todos los números del -10 al 0 [-10, -9, -8, ..., 0]')
   numeros = list( range(-10,1))
   print (numeros)
   print('\n')
   
   print('Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]')
   numeros = list( range(0,21,2))
   print (numeros)
   print('\n')
   
   print('Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]]')
   impares = []
   numeros = list( range(-20,1,1))   
   candidad = len(numeros) -1
   condicion =True 
   cont =0
   while (condicion ==True):
      if (cont > candidad):
            condicion = False
      else:          
         posibleimpar = numeros[cont]
         residuo =posibleimpar %2
         if (residuo >0):
            impares.insert(cont, posibleimpar) 
         condicion = True
         cont = cont +1
      
     
   print (impares)
   print('\n')   
   print('Todos los números múltiplos de 5 del 0 al 50 [0, 5, 10, ..., 50]')
   numeros = list( range(0,51,5))
   print (numeros)
   print('\n')
   print('FIN, muchas gracias')   
    
    
#Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas,
#pero no debe repetise ningún elemento en la nueva lista:
def ejercicio8():
   print('----------------------------------')
   print ('8) Generación de una tercera lista con los elementos repetidos de las dos primeras listas')
   print('----------------------------------')
   print('\n')
   
   condicion =True
   while (condicion ==True):
      try:      
        
         primera = int(input('Ingrese la cantidad de numeros para la primera lista: (Debe ser un numero entero positivo mayor a cero) ==>> '))
         if (primera <=0):
                condicion =True
         else:
            condicion =False                  
            
      except ValueError:
         condicion =True            
     
   condicion =True
   my_other_list = []   
   cont =0
   while (condicion ==True):
      try:      
         numero = int(input('Ingrese un número para la primera lista ==>> '))
         my_other_list.insert(cont, numero)          
         cont= cont+1  
         if (cont <= primera -1):                
               condicion =True   
         else: condicion =False 
         
      except ValueError:
         condicion =True    
   
   print('Los numeros ingresados para la primera lista son : ' + str( my_other_list))
   
   condicion =True
   while (condicion ==True):
      try:      
        
         segunda = int(input('Ingrese la cantidad de numeros para la segunda lista: (Debe ser un numero entero positivo mayor a cero) ==>> '))
         if (segunda <=0):
                condicion =True
         else:
            condicion =False                  
            
      except ValueError:
         condicion =True            
     
   condicion =True
   my_other_list2 = []   
   cont =0
   while (condicion ==True):
      try:      
         numero = int(input('Ingrese un número para la segunda lista ==>> '))
         my_other_list2.insert(cont, numero)          
         cont= cont+1  
         if (cont <= segunda -1):                
               condicion =True   
         else: condicion =False 
         
      except ValueError:
         condicion =True    
   
   print('Los numeros ingresados para la segunda lista son : ' + str( my_other_list2))
   
   longitudL1 = len (my_other_list)
   longitudL2 = len (my_other_list2)
   
   repetidos = []
   unique_repetidos = []
   
   
   if (longitudL1 <= longitudL2):
      for element in my_other_list2:
        for element1 in my_other_list:
               if (element1 == element):
                      repetidos.insert(cont, element1) 
                      
      for repetido in repetidos:
         if repetido not in unique_repetidos:
            unique_repetidos.append(repetido)  
        
   else:
      for element in my_other_list:
         for element1 in my_other_list2:
            if (element1 == element):
                     repetidos.insert(cont, element1) 
                     
                     
      for repetido in repetidos:
         if repetido not in unique_repetidos:
            unique_repetidos.append(repetido)     
          
   print ('Los números repetidos entre las dos listas son ==>> ' + str(unique_repetidos))
   print('\n')
   print('FIN, muchas gracias')   
###FIN DE FUNCIONES


###MENU PRINCIPAL   
print("----------------------------------------")
print ("Resolución de la ACTIVIDAD 2")
print("----------------------------------------")

print('\n')


nombre = input('¿Cuál es su nombre? ')
     
print ('Bienvenido ' + nombre + ", por favor seleccione una opcion para el ejercicio que desea trabajar:")
print('\n')


#Seleccion de una opción para el ejercicio

my_condition =True
while (my_condition ==True):
   try:
      
      print('Escoja 1 o 2 o 3 o 4 o 5 o 6 o 7 u 8 o 9:  ')
      print('\n')
      opcion = int(input ('\t Ejercicio 1: Dias de vacaciones de la compañía multinacional Rap  \n \t Ejercicio 2: Calculadora . \n \t Ejercicio 3: Ingreso de numero impar. \n \t Ejercicio 4: Sume de todos los números enteros pares desde el 0 hasta el 100 \n \t Ejercicio 5: Media Aritmetica  \n \t Ejercicio 6: Encontrar número en la lista  \n \t Ejercicio 7: Generar listas \n \t Ejercicio 8: Lista no repetida \n \t SALIR 9:  \n ==>>'))
             
      if opcion == 1:
         ejercicio1()
         my_condition = False
         
      elif opcion == 2:
         ejercicio2()
         my_condition = False
         
      elif opcion == 3:
         ejercicio3()
         my_condition = False
         
      elif opcion == 4:
         ejercicio4()
         my_condition = False
         
      elif opcion == 5:
         ejercicio5()
         my_condition = False
      
      elif opcion == 6:
         ejercicio6()
         my_condition = False
         
      elif opcion == 7:
         ejercicio7()
         my_condition = False
         
      elif opcion == 8:
         ejercicio8()
         my_condition = False   
      
      elif opcion == 9:            
         my_condition = False
         print('FIN, muchas gracias')     
      else:
         my_condition =True
          
   except ValueError:
      my_condition =True
        
###FIN DEL MENU PRINCIPAL   