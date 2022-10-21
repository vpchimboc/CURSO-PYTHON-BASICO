print("Calculadora con una sola variable \n")

print("********************")
print("* Menú de opciones *")
print("********************")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Modulo o resto \n")

numero = int(input("Introduce la opción deseada:"))

if numero == 1:

    print("Eligste suma \n")
    numero = int(input("Introduce el primer número:"))
    numero += int(input("Introduce el segundo número:"))
    print("El resultado de la suma es:", numero)

elif numero == 2:

    print("Eligste resta \n")
    numero = int(input("Introduce el primer número:"))
    numero -= int(input("Introduce el segundo número:"))
    print("El resultado de la resta es:", numero)

elif numero == 3:

    print("Eligste multiplicación \n")
    numero = int(input("Introduce el primer número:"))
    numero *= int(input("Introduce el segundo número:"))
    print("El resultado de la multiplicación es:", numero)

elif numero == 4:

    print("Eligste división \n")
    numero = float(input("Introduce el primer número:"))
    numero /= float(input("Introduce el segundo número:"))
    print("El resultado de la división es:", round(numero, 2))

elif numero == 5:

    print("Eligste divisón entera \n")
    numero = int(input("Introduce el primer número:"))
    numero //= int(input("Introduce el segundo número:"))
    print("El resultado de la división entera es:", numero)

elif numero == 6:

    print("Eligste exponente \n")
    numero = int(input("Introduce el primer número:"))
    numero **= int(input("Introduce el segundo número:"))
    print("El resultado del exponente es:", numero)

elif numero == 7:

    print("Eligste módulo o resto \n")
    numero = int(input("Introduce el primer número:"))
    numero %= int(input("Introduce el segundo número:"))
    print("El módulo o resto es:", numero)

else:
    print("La opción elegida no existe, vuelve a intentar.")






























