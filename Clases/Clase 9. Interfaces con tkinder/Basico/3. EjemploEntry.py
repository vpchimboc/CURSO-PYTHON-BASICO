from re import L
from tkinter import *
raiz=Tk()
miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()
minombre=StringVar()

cuadroNombre=Entry(miFrame,textvariable=minombre)
#cuadroNombre.place(x=100,y=100)
cuadroNombre.grid(row=0,column=1,pady=5)
cuadroNombre.config(fg="red",justify="center")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3,column=1,pady=5)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1,pady=5)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2,column=1,pady=5)


nombreLabel=Label(miFrame,text="Nombre: ")
#nombreLabel.place(x=100,y=100)
nombreLabel.grid(row=0,column=0, pady=5,sticky="e")

apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=1,column=0,pady=5, sticky="e")

direccionLabel=Label(miFrame,text="Dirección: ")
direccionLabel.grid(row=2,column=0, pady=5,sticky="e")

passLabel=Label(miFrame,text="Password: ")
passLabel.grid(row=3,column=0, pady=5,sticky="e")

#Area de texto
textoComentario=Text(miFrame,width=13,height=5)
textoComentario.grid(row=4,column=1, pady=5)
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=4,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

comentariosLabel=Label(miFrame,text="Comentarios: ")
comentariosLabel.grid(row=4,column=0, pady=5,sticky="e")

#Botones
def codigoBoton():
    minombre.set("Veronica")
    print(cuadroNombre.get())
    
botonEnvio=Button(raiz,text="Enviar", command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()