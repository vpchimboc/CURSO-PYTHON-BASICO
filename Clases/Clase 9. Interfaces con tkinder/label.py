from email.mime import image
from tkinter import*

root=Tk()
#Cambiar el texto dinámicamente
texto_nuevo=StringVar()
texto_nuevo.set("Python")
root.title("Bienvenidos")
root.config(width=300,height=200)#Especificamos tamaño de la ventaa
#Creamos un label
label=Label(root,text="Hola mundo")
#Especifica la posición del label
label.place(x=10,y=10)
#Agregamos color de background
label.config(bg="blue",fg="red",font=("Curier",20))

label=Label(root,text="Bienvenidos")
label.place(x=10,y=50)
#Agregamos color de background
label.config(bg="green",fg="blue",font=("Curier",20),textvariable=texto_nuevo)

##Agregar una imagen
imagen=PhotoImage(file="imagen.gif")
label=Label(root,image=imagen)
label.place(x=50,y=90)

root.mainloop()