#https://python-docs-es.readthedocs.io/es/3.10/library/tkinter.html#tkinter-life-preserver

from tkinter import*
#Creamos la ventana
root=Tk()
#Para agregar un título
root.title("Verónica")
#modificar el tamaño de la ventana
root.resizable(0,0)#No se modifica ni ancho y alto
root.resizable(0,1)#Se modifica en lo ancho y alto
root.resizable(True,True)#Se modifica en lo ancho y alto
#Cambiar la imagen
root.iconbitmap("hola.ico")
#Presentamos la ventana
root.mainloop()