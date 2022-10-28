from tkinter import *

root=Tk()
barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

archivoMenu=Menu(barraMenu,tearoff=0)
archivoEdicion=Menu(barraMenu,tearoff=0)
archivoHerramientas=Menu(barraMenu,tearoff=0)
archivoAyuda=Menu(barraMenu,tearoff=0)

#menus a la barra
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Eición",menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

#Submenus de menu archivo
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

#Submenus de menu edicion
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

#Submenus de menu ayuda
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de")


root.mainloop()