from tkinter import *
raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()

#.........pantalla........
pantalla=Entry(miFrame)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="black", fg="green", justify="right")
#.......Fila 1...........
boton7=Button(miFrame,text="7",width=3)
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text="8",width=3)
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text="9",width=3)
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame,text="/",width=3)
botonDiv.grid(row=2,column=4)
#.......Fila 2...........
boton4=Button(miFrame,text="4",width=3)
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text="5",width=3)
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text="6",width=3)
boton6.grid(row=3,column=3)
botonMult=Button(miFrame,text="*",width=3)
botonMult.grid(row=3,column=4)

#.......Fila 3...........
boton1=Button(miFrame,text="1",width=3)
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text="2",width=3)
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text="3",width=3)
boton3.grid(row=4,column=3)
botonRest=Button(miFrame,text="*",width=3)
botonRest.grid(row=4,column=4)
#.......Fila 3...........
boton0=Button(miFrame,text="0",width=3)
boton0.grid(row=4,column=1)
botonComa=Button(miFrame,text=",",width=3)
botonComa.grid(row=4,column=2)
botonIgual=Button(miFrame,text="=",width=3)
botonIgual.grid(row=4,column=3)
botonSum=Button(miFrame,text="+",width=3)
botonSum.grid(row=4,column=4)

raiz.mainloop()