#Recorriendo los elementos de una lista utilizando While
numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice+=1

#Sentencia For (Para) con listas
for numero in numeros:  # Para [variable] en [lista]
    print(numero)

#For con cadenas
cadena = "Hola amigos"
for caracter in cadena:
    print(caracter)

#La función range()
#Sirve para generar una lista de números que podemos recorrer fácilmente, pero no ocupa memoria porque se interpreta sobre la marcha:
for i in range(10):
    print(i)

print(range(10))