print("=========")
print("Conversor")
print("========= \n")

print("Menú de opciones: \n")
print("Presiona 1 para convertir de número a palabra.")
print("Presiona 2 para convertir de palabra a número. \n")

opcion = int(input("¿Cúal es tu opción deseada?:"))

if opcion == 1:
    print("\n Conversor de número a palabra. \n")

    opcion_uno = int(input("¿Cúal es el número que deseas convertir a palabra?: "))

    if opcion_uno == 1:
        print("El número es 'UNO'")
    elif opcion_uno == 2:
        print("El número es 'DOS'")
    elif opcion_uno == 3:
        print("El número es 'TRES'")
    elif opcion_uno == 4:
        print("El número es 'CUATRO'")
    elif opcion_uno == 5:
        print("El número es 'CINCO'")
    else:
        print("El número seleccionado no esta registrado.")    

elif opcion == 2:
    print("\n Conversor de palabra a número. \n")

    opcion_dos = input("¿Cual es la plabra que deseas convertir a número?: ")
    opcion_dos = opcion_dos.lower()

    if opcion_dos == "uno":
        print("El número es '1'")
    elif opcion_dos == "dos":
        print("El número es '2'")
    elif opcion_dos == "tres":
        print("El número es '3'")
    elif opcion_dos == "cuatro":
        print("El número es '4'")
    elif opcion_dos == "cinco":
        print("El número es '5'")
    else:
        print("El número seleccionado no esta registrado.")

else:
    print("Opción no disponible.")

print("Fin.")





















