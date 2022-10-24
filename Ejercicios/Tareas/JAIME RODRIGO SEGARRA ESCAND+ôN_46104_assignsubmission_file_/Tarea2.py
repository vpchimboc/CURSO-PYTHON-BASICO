#Problema 1
from ctypes.wintypes import PINT


nom=input("Ingrese su nombre:")
clave=float (input("Ingrese la clave del departamento: "))
ant=float (input("Ingrese la antigüedad: "))

if (clave==1):
    if (ant==1):
        print(nom, " recibirá 6 días de vacaciones")
    if (ant > 2 and ant < 7):
        print(nom, " recibirá 14 días de vacaciones")
    if (ant> 6):
        print(nom, " recibirá 20 días de vacaciones")

if (clave==2):
    if (ant==1):
        print(nom, " recibirá 7 días de vacaciones")
    if (ant > 2 and ant < 7):
        print(nom, " recibirá 15 días de vacaciones")
    if (ant> 6):
        print(nom, " recibirá 22 días de vacaciones")

#Problema 2
num1=float (input("Ingrese el primer número: "))
num2=float (input("Ingrese el segundo número: "))
ban=0
while ban < 4:
    print ("1. Resta de los dos números")
    print ("2. Suma de los dos números")
    print ("3. Multiplicación de los dos números")
    print ("4. Salir")
    num=float (input("Dígite un número entre 1 y 4: "))
    if (num==1):
        x=num1+num2
        print ("La suma es de los dos números es: ", x)
        ban=5
    if (num==2):
        x=num1-num2
        print ("La resta es de los dos números es: ", x)
        ban=5
    if (num==4):
         ban=5
    if (num> 4 or num< 1):
        print("Ingrese un valor correcto")
        ban=0
#Problema 3
ban=0
while ban < 2:
    
    num=float (input("Ingrese un número impar: "))
    if (num%2==0):
        print ("número incorrecto, ingrese otro valor")
        ban=0
    else:
        print ("número correcto")
        ban=6
#PROBLEMA 4
ban=0
sum=0

while ban < 100:
    ban=ban+2
    sum=sum+ban
print ("La suma de los números pares es: ", sum)   

#PROBLEMA 5
ban=0
sum=0
num=float(input("¿Cuántos números va a ingresar: "))

while ban < num:
    ban=ban+1
    num1=float(input("¿Ingrese el número: ")) 
    sum=sum+num1
prom=sum/ban    
print("El promedio es:", round (prom,2))