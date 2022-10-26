from tkinter import*
from turtle import left
#Creamos la ventana
root=Tk()
#Para agregar un título
root.title("Verónica")
#modificar el tamaño de la ventana
root.resizable(0,0)#No se modifica ni ancho y alto
root.resizable(1,1)#Se modifica en lo ancho y alto
root.resizable(True,True)#Se modifica en lo ancho y alto
#Cambiar la imagen
root.iconbitmap("hola.ico")
#root.geometry("600x300")#Para asignarle un tamaño a la ventana
#Creamos un Frame
miFrame=Frame(root)
#empaquetamos el frame a la ventana principal
miFrame.pack(side=RIGHT, anchor="n")#Side permite especificar la ubicación del Frame en pantalla
miFrame.pack(fill="x",expand=1)#Expand y fill es para poder especificar el frame dentro
#agregamos un tamaño al frame
miFrame.config(width=600,height=300)
#cambiar de cursor
miFrame.config(cursor="pirate")
#Cambiar de color al Frame
miFrame.config(bg="blue")
#Agregar un borde al Frame
miFrame.config(bd="20")
#Agregar un borde al Frame
miFrame.config(relief="ridge")

#cambiar de cursor de la ventana
root.config(cursor="boat")
#Cambiar de color al Frame
root.config(bg="blue")
#Agregar un borde al Frame
root.config(bd="25")
#Agregar un borde al Frame
root.config(relief="sunken")
#Presentamos la ventana
root.mainloop()