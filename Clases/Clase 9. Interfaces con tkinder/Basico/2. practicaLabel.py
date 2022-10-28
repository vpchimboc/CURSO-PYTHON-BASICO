from tkinter import *
root=Tk()
miFrame=Frame(root,width=500,height=400)
miFrame.pack()
miLabel=Label(miFrame,text="Hola Alumnos de Python")
#miLabel.pack()
miLabel.place(x=100,y=200)
miLabel.config(fg="red",font=("Comic Sans MS",18))
#####imagen
miImagen=PhotoImage(file="imagen.png")
miLabel2=Label(miFrame,image=miImagen)
miLabel2.place(x=100,y=10)
root.mainloop()
