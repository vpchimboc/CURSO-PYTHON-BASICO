print("***************************************************************************")
print("* Programa para determinar ¿Cúal es el número más grande de tres números? *")
print("*************************************************************************** \n")

num_uno = int(input("Introduce el primer número:"))
num_dos = int(input("Introduce el segundo número:"))
num_tres = int(input("Introduce el tercer número:"))

if num_uno > num_dos and num_uno > num_tres:
    print("El número ", num_uno, " es el número más grande de los tres.")
else:
    if num_dos > num_tres:
        print("El número ", num_dos, " es el número más grande de los tres.")
    else:
        print("El número ", num_tres, " es el número más grande de los tres.")
