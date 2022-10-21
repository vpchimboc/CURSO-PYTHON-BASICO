"""Ciclo whie
Permite ejecutar en repetidas ocasiones las instrucciones
o líneas de código indicadas por el programador, con lo cual,
no exixte la necesidad de duplicar líneas de código para ejecutarlas
en más de una ocasión
Permite repetir la ejecución de un grupo de instrucciones, mientras se cumpla una
condición, ede decir, mientras la condición del ciclo o bucle se cumpla las instrucciones
se seguiran ejecutando
"""
#Ejemplo 1. Imprimir los 100 primero numeros
"""cont=0
while cont<=100:
    print("",cont)
    cont+=1
else:
    print("Finaliza")
#Ejemplo 2. Imprimir el nombre 1000
x=1
while x<11:
    print("Veronica")
"""
"""Imprimir la serie fibonaci 
Desarrollar un programa que imprima en pantalla
la Siucesión de Fibonacci desde el número 0 hasta 
el número 1596, de manera horizontal
Requerimientos indispensables 
El programa debera tener un máximo de 7 líneas de códigos

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 
"""

"""
Patricio Pacheco
f,a0,a1=0,1,0
while(f<=1597):
    print(f,end=" ")
    f = a1 + a0
    a0,a1=a1,f
"""
"""
Carmen Tacuri 

print("Serie Fibonacci : ")

n=int(input("Ingrese un numero 'n': "))

primero, segundo, sum, count =  0,1,0,1



while(count<=n):    
  print(sum, end=" ")
  count+=1
  primero=segundo
  segundo=sum
  sum=primero+segundo	
  """
first, second, sum, count=0,1,0,1
print("Serie Fibonaci")
while(count<=18):
  print(sum, end=" ")
  count+=1 
  first,second=second,sum
  sum=first+second

# fibonaci Boris Suquilanda
cont,fibo1,fibo2=0,1,0
while cont<=1597:
    print(cont,end=" ")
    cont=fibo2+fibo1
    fibo1,fibo2=fibo2,cont
else:
    print("Finaliza")

# Raul Mejía

print("Serie Fibonaci")
valorI,valorF,resul=0,1,0
print(valorI,valorF,end=(" "))
while resul<=1507:
    resul=valorI+valorF
    valorI,valorF=valorF,resul
    print(resul,end=(" "))
    

#VeronicaS
a,b,c=0,1,0
while a<=1598:
    print(a,end="  ")
    c=a+b
    a,b=b,c
else:
    print("Finaliza")

    
# @Creado y modificado por LADY SANGACHA
a,b= 0,1
limit = 2800
print("LA SERIE FIBONNACI ES :")
while(b <= limit):
    print(a, end=(" "))
    a,b = b,a+b
