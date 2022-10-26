from tkinter import Tk, PhotoImage, Label
# from tkinter import PhotoImage

app = Tk()
app.title("Bienvenidos")
app.config(width=800,height=300)#Especificamos tamaño de la ventaa
# Lees la imagen:
# He colocado ruta relativa, es decir, la imagen a la misma 
# altura de la aplicación. Si prefieres, puedes colocar una
# ruta absoluta.
imagen = PhotoImage(file = "python_logo.png")

# Con Label y la opción image, puedes mostrar una imagen en el widget:
background = Label(image = imagen, text = "Imagen S.O de fondo")

# Con place puedes organizar el widget de la imagen posicionandolo
# donde lo necesites (relwidth y relheight son alto y ancho en píxeles):
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Por defecto el fondo es blaco. Accediendo al método config
# de Label podrías, por ejemplo, establecer un color de fondo distinto:
# background.config(bg = "gray")
#Creamos un label
label=Label(app,text="BIENVENIDOS AL CURSO")
#Especifica la posición del label
label.place(x=150,y=20)
#Agregamos color de background
label.config(bg="blue",fg="red",font=("Curier",30))

app.mainloop()